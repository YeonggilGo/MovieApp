<template>
  <carousel
    class="carousel"
    :perPage="1"
    :navigationEnabled="true"
    :paginationEnabled="false"
    navigationNextLabel="&rsaquo;"
    navigationPrevLabel="&lsaquo;"
  >
    <slide :key="genre" v-for="(genre, idx) in genres">
      <MovieCarouselItem :genre="genre" :imageSrc="imageSrcs[idx]" />
    </slide>
  </carousel>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel';

import MovieCarouselItem from './MovieCarouselItem.vue';

import actionImage from '../../assets/images/action.jpg';
import thrillerImage from '../../assets/images/thriller.jpg';
import dramaImage from '../../assets/images/drama.jpg';
import criminalImage from '../../assets/images/criminal.jpg';

export default {
  name: 'MovieCarousel',
  components: {
    Carousel,
    Slide,
    MovieCarouselItem,
  },
  data: function() {
    return {
      genres: ['action', 'thriller', 'drama', 'criminal'],
      imageSrcs: [actionImage, thrillerImage, dramaImage, criminalImage],
    };
  },
};
</script>

<style lang="scss">
.carousel {
  position: relative;
}

.VueCarousel-navigation-prev,
.VueCarousel-navigation-next {
  color: #fff !important;
  font-size: 4rem;
}

.VueCarousel-navigation-prev {
  left: 60px !important;
}

.VueCarousel-navigation-next {
  right: 60px !important;
}
</style>
