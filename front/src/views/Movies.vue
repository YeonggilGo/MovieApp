<template>
  <div class="movies_container">
    <div class="movies_inner">
      <h1 class="title">{{ title }}</h1>
      <category-tabs :currentTab="$route.params.category" />
      <div class="movies">
        <movie-card
          :key="movie.id"
          v-for="movie in category !== 'popular' && category !== 'recommend'
            ? $store.state.movie.movies.slice(0, page * 20)
            : $store.state.movie.movies"
          :movie="movie"
        />
      </div>
      <button
        class="more_movies"
        v-if="
          category !== 'popular' &&
            category !== 'recommend' &&
            page <= $store.state.movie.movies.length
        "
        @click="onClickMoreMoviesButton"
      >
        더보기 <i class="fas fa-angle-down"></i>
      </button>
    </div>
  </div>
</template>

<script>
import movieStatic from '../assets/js/movie';

import MovieCard from '../components/movie/MovieCard.vue';
import CategoryTabs from '../components/movie/CategoryTabs.vue';

export default {
  name: 'Movies',
  data: function() {
    return {
      page: 1,
    };
  },
  methods: {
    getTabUrl: function(tab) {
      return `/movies/${tab}`;
    },
    getMovies: function() {
      const category = this.$route.params.category;

      if (category === 'all') {
        this.$store.dispatch('getAllMovies');
        return;
      }

      if (category === 'popular') {
        this.$store.dispatch('getPopularMovies');
        return;
      }

      if (category === 'recommend') {
        this.$store.dispatch('getRecommendMovies');
        return;
      }

      this.$store.dispatch('getGenreMovies', movieStatic.genre_ids[category]);
    },
    onClickMoreMoviesButton: function() {
      this.page += 1;
    },
  },
  components: {
    MovieCard,
    CategoryTabs,
  },
  computed: {
    title: function() {
      return movieStatic.category[this.$route.params.category];
    },
    category: function() {
      return this.$route.params.category;
    },
  },
  watch: {
    category: function() {
      this.getMovies();
      this.page = 1;
    },
  },
  created: function() {
    this.getMovies();
  },
};
</script>

<style lang="scss" scoped>
.movies_container {
  padding: 30px 0;

  .movies_inner {
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

    .more_movies {
      all: unset;
      cursor: pointer;
      display: block;
      font-size: 1.1rem;
      margin-top: 20px;
      padding: 20px 0;
      text-align: center;
      width: 100%;

      i {
        margin-left: 5px;
      }
    }
  }
}
</style>
