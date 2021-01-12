<template>
  <div class="search_container">
    <div class="search_inner">
      <h1 class="title">
        검색 결과: {{ $route.query.searchTerm }} ({{
          $store.state.movie.movies.length
        }}개)
      </h1>
      <div class="movies">
        <movie-card
          :key="movie.id"
          v-for="movie in $store.state.movie.movies"
          :movie="movie"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCard from '../components/movie/MovieCard.vue';

export default {
  name: 'Search',
  components: {
    MovieCard,
  },
  created: function() {
    this.$store.dispatch('searchMovies', this.$route.query.searchTerm);
  },
  computed: {
    searchTerm: function() {
      return this.$route.query.searchTerm;
    },
  },
  watch: {
    searchTerm: function() {
      this.$store.dispatch('searchMovies', this.searchTerm);
    },
  },
};
</script>

<style lang="scss" scoped>
.search_container {
  padding: 30px 0;

  .search_inner {
    margin: 0 auto;
    max-width: 1200px;
    width: 100%;

    .title {
      font-size: 1.8rem;
      font-weight: normal;
      margin-bottom: 30px;
    }

    .movies {
      display: grid;
      gap: 60px;
      grid-template-columns: repeat(4, minmax(255px, 1fr));
      width: 100%;
    }
  }
}
</style>
