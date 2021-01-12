<template>
  <div class="movie_detail_container">
    <MovieInfo :movie="$store.state.movie.movie" />
    <MovieReviews :reviews="[]" :movie="$store.state.movie.movie" />
  </div>
</template>

<script>
import MovieInfo from '../components/movie/MovieInfo.vue';
import MovieReviews from '../components/movie/MovieReviews.vue';

export default {
  name: 'MovieDetail',
  components: {
    MovieInfo,
    MovieReviews,
  },
  created: function() {
    this.$store.dispatch('getMovieDetail', this.$route.params.id);
  },
};
</script>

<style></style>
