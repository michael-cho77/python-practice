from dataclasses import asdict
from typing import Any

from motor.motor_asyncio import AsyncIOMotorCollection

from app.entities.category.category_codes import CategoryCode
from app.entities.collections.geo_json import GeoJsonPoint, GeoJsonPolygon
from app.entities.collections.shop.shop_document import (
    ShopDeliveryAreaSubDocument,
    ShopDocument,
)
from app.utils.mongo import db


class ShopCollection:
    _collection = AsyncIOMotorCollection(db, "shops")

    @classmethod
    async def point_intersects(cls, point: GeoJsonPoint) -> list[ShopDocument]:
        return [
            cls._parse(result)
            #  $geoIntersects -> “delivery_areas.poly 폴리곤과 point 가 서로 겹치면, 그 document 를 가져옴”
            for result in await cls._collection.find(
                {"delivery_areas.poly": {"$geoIntersects": {"$geometry": asdict(point)}}}
            ).to_list(length=None)
        ]

    @classmethod
    async def insert_one(
        cls, name: str, category_codes: list[CategoryCode], delivery_areas: list[ShopDeliveryAreaSubDocument]
    ) -> ShopDocument:
        result = await cls._collection.insert_one(
            {
                "name": name,
                "category_codes": category_codes,
                "delivery_areas": [asdict(delivery_area) for delivery_area in delivery_areas],
            }
        )

        return ShopDocument(
            _id=result.inserted_id, name=name, category_codes=category_codes, delivery_areas=delivery_areas
        )

    @classmethod
    def _parse(cls, result: dict[Any, Any]) -> ShopDocument:
        return ShopDocument(
            _id=result["_id"],
            name=result["name"],
            delivery_areas=[
                ShopDeliveryAreaSubDocument(poly=GeoJsonPolygon(coordinates=delivery_area["poly"]["coordinates"]))
                for delivery_area in result["delivery_areas"]
            ],
            category_codes=[CategoryCode(category_code) for category_code in result["category_codes"]],
        )
