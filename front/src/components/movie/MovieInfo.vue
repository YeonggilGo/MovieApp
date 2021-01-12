<template>
  <div
    class="movie_info"
    :style="{
      background: getBackgroundStyle(movie.backdrop_path, true),
    }"
    v-if="JSON.stringify(movie) !== '{}'"
  >
    <div class="info_inner">
      <div
        class="poster"
        :style="{
          background: getBackgroundStyle(movie.poster_path),
        }"
      />

      <div class="infos">
        <h1 class="title">{{ movie.title }}</h1>
        <p class="original_title">{{ movie.origin_title }}</p>
        <div class="rating_popularity">
          <div class="rating">
            <div class="tit">관람객 평점</div>
            <div class="cont">
              <i class="fas fa-star"></i> {{ movie.vote_average }}
            </div>
          </div>
          <div class="popularity">
            <div class="tit">인기도</div>
            <div class="cont">{{ movie.popularity }}</div>
          </div>
          <button type="button" class="like_button">
            <i class="fas fa-heart" v-if="liked" @click="onClickLikeButton"></i>
            <i
              class="far fa-heart"
              v-if="!liked"
              @click="onClickLikeButton"
            ></i>
          </button>
        </div>
        <hr
          style="border: 1px solid rgba(255, 255, 255, 0.6); margin: 20px 0;"
        />
        <div class="genres">
          <div class="tit">장르</div>
          <div class="cont">{{ getGenres(movie.genres) }}</div>
        </div>
        <div class="release_date">
          <div class="tit">개봉일</div>
          <div class="cont">{{ getReleaseDate(movie.release_date) }}</div>
        </div>
        <div class="overview">
          <div class="tit">줄거리 요약</div>
          <div class="cont">{{ getOverview(movie.overview) }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import moment from 'moment';
import { mapState } from 'vuex';

import movieInfo from '../../assets/js/movie';

export default {
  name: 'MovieInfo',
  props: {
    movie: Object,
  },
  data: function() {
    return {
      genres: {},
    };
  },
  methods: {
    getGenres: function(genre_ids) {
      return genre_ids.map(id => this.genres[id]).join(', ');
    },
    getBackgroundStyle: function(imageUrl, isDark = false) {
      if (isDark) {
        return `linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(https://image.tmdb.org/t/p/w500${imageUrl}) center center/cover`;
      }
      return `url(https://image.tmdb.org/t/p/w500${imageUrl}) center center/cover`;
    },
    getReleaseDate: function(date) {
      return moment(date).format('YYYY년 M월 DD일');
    },
    getOverview: function(overview) {
      if (!overview) {
        return '줄거리 요약이 없습니다.';
      }
      return overview;
    },
    onClickLikeButton: function() {
      this.$store.dispatch('likeMovie', this.movie.id);
    },
  },
  computed: {
    ...mapState({
      liked: state => state.movie.movie.liked,
    }),
  },
  created: function() {
    this.genres = movieInfo.genres;
  },
};
</script>

<style lang="scss" scoped>
.movie_info {
  color: #fff;
  height: 700px;
  position: relative;
  width: 100%;

  .info_inner {
    align-items: center;
    display: flex;
    height: 100%;
    margin: 0 auto;
    max-width: 1200px;
    width: 100%;

    .poster {
      border-radius: 4px;
      height: 600px;
      margin-right: 100px;
      width: 400px;
    }

    .infos {
      height: 100%;
      padding: 50px 0;
      max-width: calc(100% - 500px);

      .title {
        font-size: 3.5rem;
      }

      .original_title {
        color: rgba(255, 255, 255, 0.6);
        font-size: 1.1rem;
        margin-bottom: 50px;
      }

      .tit {
        color: rgba(255, 255, 255, 0.7);
        font-size: 1rem;
        margin-right: 20px;
      }

      .cont {
        align-items: center;
        display: flex;
        font-size: 1rem;
      }

      .rating_popularity,
      .genres,
      .release_date {
        align-items: center;
        display: flex;
      }

      .overview {
        .tit {
          margin-bottom: 10px;
        }
      }

      .rating,
      .popularity {
        align-items: center;
        display: flex;
      }

      .like_button {
        all: unset;
        color: #ff0000;
        cursor: pointer;
        margin-left: 40px;
      }

      .rating {
        margin-right: 40px;

        i {
          color: #ffda77;
          font-size: 0.7rem;
          margin-right: 3px;
        }
      }

      .genres {
        margin-bottom: 10px;
      }

      .release_date {
        margin-bottom: 50px;
      }
    }
  }
}
</style>
