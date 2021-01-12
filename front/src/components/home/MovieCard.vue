<template>
  <router-link
    class="movie"
    :to="{ name: 'MovieDetail', params: { id: movie.id } }"
    :key="movie.id"
  >
    <div class="poster_wrapper">
      <div class="movie_poster" :style="'background: ' + backgroundStyle" />
    </div>

    <div class="title_rating">
      <div class="movie_title">{{ movie.title }}</div>
      <div class="movie_rating">
        <i class="fas fa-star"></i> {{ movie.vote_average }}
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  data: function() {
    return {
      backgroundStyle: `url(https://image.tmdb.org/t/p/w500${this.movie.poster_path}) center center/cover`,
    };
  },
};
</script>

<style lang="scss" scoped>
.movie {
  text-decoration: none;
  width: 224px;

  & + .movie {
    margin-left: 20px;
  }

  .poster_wrapper {
    overflow: hidden;

    .movie_poster {
      height: 320px;
      transition: 0.5s;
      width: 100%;

      &:hover {
        transform: scale(1.1);
      }
    }
  }

  .title_rating {
    align-items: center;
    display: flex;
    justify-content: space-between;

    .movie_title {
      color: #595959;
      font-size: 1rem;
      font-weight: bold;
      overflow: hidden;
      padding: 5px;
      text-overflow: ellipsis;
      white-space: nowrap;
      width: 100%;
    }

    .movie_rating {
      align-items: center;
      display: flex;
      font-size: 0.8rem;

      i {
        color: #ffda77;
        font-size: 0.7rem;
        margin-right: 3px;
      }
    }
  }
}
</style>
