import {
    FavoriteBorderOutlined,
    SearchOutlined,
    ShoppingCartOutlined,
  } from "@material-ui/icons";
  import styled from "styled-components";

  const Container= styled.div`
  margin-bottom: 15px;
  `;
  
  const Info = styled.div`
    opacity: 0;
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.2);
    z-index: 3;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.5s ease;
    cursor: pointer;
  `;
  
  const ImageContainer = styled.div`
    flex: 1;
    margin: 5px;
    min-width: 280px;
    height: 350px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f5f5f5;
    position: relative;
    &:hover ${Info}{
      opacity: 1;
    }
  `;
  
  const Circle = styled.div`
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background-color: white;
    position: absolute;
  `;
  
  const Image = styled.img`
    height: 75%;
    z-index: 2;
  `;
  
  const Icon = styled.div`
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 10px;
    transition: all 0.5s ease;
    &:hover {
      background-color: #e9f5f5;
      transform: scale(1.1);
    }
  `;

const ProductContainer = styled.div`
    display: flex;
    justify-content: space-between;
    word-break: keep-all;
    line-height: 1.6em;
    letter-spacing: -1px;
    padding: 0px 10px 0px 20px;
`;

const ProductDisplay = styled.div`
width: 66.666666666%;
`;


const ProductStatus = styled.div`
    height: 24px; 
    font-size: 0.8rem;
    color: #fe0000;
`;

const ProductName = styled.p`
line-height: 1.4em;
font-size: 0.9rem;

& span{
    display: block;
    white-space: pre-wrap;
    word-break: break-all;
}
`;

const ProductCategory = styled.span`
  color:#8d8d8d;
  font-size: 0.8rem;
`;

const ProductPrice = styled.div`
 padding-right: 10px;
 font-size: 0.9rem;
`;
  
  const Product = ({ item }) => {
    return (
      <>
      <Container>
        <ImageContainer>
          <Circle />
          <Image src={item.img} />
          <Info>
            <Icon>
              <ShoppingCartOutlined />
            </Icon>
            <Icon>
              <SearchOutlined />
            </Icon>
            <Icon>
              <FavoriteBorderOutlined />
            </Icon>
          </Info>
        </ImageContainer>
        <ProductContainer>
          <ProductDisplay>
            <ProductStatus>품절</ProductStatus>
            <ProductName>
              <span>Good Stuff</span>
            </ProductName>
            <ProductCategory>Cloth</ProductCategory>
          </ProductDisplay>
          <ProductPrice> 139,000 원</ProductPrice>
        </ProductContainer>
      </Container>

    </>
    );
  };
  
  export default Product;