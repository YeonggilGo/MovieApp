<template>
  <div class="popular_movies">
    <div class="header"><span class="first_letter">P</span>OPULAR</div>
    <div class="movies">
      <movie-card :key="movie.id" :movie="movie" v-for="movie in movies" />
    </div>
  </div>
</template>

<script>
import axiosClient from '../../lib/axiosClient';

import MovieCard from './MovieCard.vue';

export default {
  name: 'popularMovies',
  components: {
    MovieCard,
  },
  data: function() {
    return {
      movies: [],
    };
  },
  created: function() {
    axiosClient
      .get('/movies/popular')
      .then(res => (this.movies = res.data.slice(0, 5)))
      .catch(e => console.error(e));
  },
};
</script>

<style lang="scss" scoped>
.popular_movies {
  margin: 0 auto;
  max-width: 1200px;
  padding-top: 100px;
  width: 100%;

  .header {
    color: #1fab89;
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 40px;

    .first_letter {
      background: #1fab89;
      color: #fff;
      display: inline-block;
      padding: 0 5px;
    }
  }

  .movies {
    display: flex;
    overflow-x: scroll;
    width: 100%;

    &::-webkit-scrollbar {
      display: none;
    }
  }
}
</style>
