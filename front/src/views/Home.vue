<template>
  <div>
    <movie-carousel />
    <popular-movies />
    <recommend-movies />
  </div>
</template>

<script>
import MovieCarousel from '../components/home/MovieCarousel.vue';
import PopularMovies from '../components/home/PopularMovies.vue';
import RecommendMovies from '../components/home/RecommendMovies.vue';

export default {
  name: 'Home',
  components: {
    MovieCarousel,
    PopularMovies,
    RecommendMovies,
  },
};
</script>

<style></style>
