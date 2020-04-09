import datetime
from django.db import models
from django.utils import timezone
from core import models as core_models


class BookedDay(core_models.TimeStampedModel):

    day = models.DateField()
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Booked Day"
        verbose_name_plural = "Booked Days"

    def __str__(self):
        return str(self.day)


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True

    def save(self, *args, **kwargs):
        # pk is None -> 생성하려는 모델이 새로운 reservation임
        if self.pk is None:
            start = self.check_in
            end = self.check_out
            difference = end - start
            # BoodedDay를 day의 range (start, end) 사이에 있는지 확인한다.
            existing_booked_day = BookedDay.objects.filter(
                day__range=(start, end)
            ).exists()

            # booked_day가 없다면 super().save()를 통해 reservation을 저장한다.
            # Booked_day는 Reservation을 외래키로 가지고 있기 때문에 먼저 Reservation이 저장되야 생성이 가능하다.
            if not existing_booked_day:
                super().save(*args, **kwargs)
                # 그 후 start ~ end 사이의 각 날짜들의 booked_day를 생성한다.
                for i in range(difference.days + 1):
                    day = start + datetime.timedelta(days=i)
                    BookedDay.objects.create(day=day, reservation=self)
                return

        return super().save(*args, **kwargs)
