import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css"; 
import "swiper/css/navigation"; 
import "swiper/css/pagination"; 
import "swiper/css/scrollbar";

import { Image } from "@chakra-ui/react";

import { Navigation, Pagination, Scrollbar, A11y } from "swiper/modules";

interface Image {
  src: string;
  alt: string;
}

interface ImageCarouselProps {
  images: Image[];
}
const ImageCarousel: React.FC<ImageCarouselProps> = ({ images }) => {
  return (
    <Swiper
      modules={[Navigation, Pagination, A11y]}
      spaceBetween={50}
      slidesPerView={1}
      navigation
      pagination={{ clickable: true }}
    >
      {images.map((image, index) => (
        <SwiperSlide key={index}>
          <Image
            src={image.src}
            alt={image.alt}
            fit="cover"
            style={{ display: "block" }}
            borderRadius={20}
          />
        </SwiperSlide>
      ))}
    </Swiper>
  );
};

export default ImageCarousel;
