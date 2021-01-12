<template>
  <div class="movie_reviews" v-if="movie">
    <div class="header"><span class="first_letter">R</span>EVIEW</div>

    <div class="summary">
      <i class="fas fa-star"></i> {{ movie.vote_average }}점 (후기
      {{ reviews.length }}개)
    </div>

    <div class="write_review">
      <div class="suggestion">
        이 영화에 대한 <strong>여러분의 소중한 의견</strong> 남겨주세요!
      </div>
      <button class="write_button" @click="onClickWriteButton">
        <i class="fas fa-pencil-alt"></i>한줄평쓰기
      </button>
    </div>

    <div class="reviews" v-if="reviews.length > 0">
      <MovieReview
        :key="review.id"
        v-for="review in reviews"
        :review="review"
      />
    </div>

    <review-modal
      :isVisible="isModalVisible"
      :onSubmit="onWriteReview"
      @close="isModalVisible = false"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex';

import MovieReview from './MovieReview.vue';
import ReviewModal from './ReviewModal.vue';

export default {
  name: 'MovieReviews',
  data: function() {
    return {
      isModalVisible: false,
    };
  },
  props: {
    movie: Object,
  },
  computed: {
    ...mapState({
      reviews: state => state.movie.reviews,
    }),
  },
  methods: {
    onClickWriteButton: function() {
      this.isModalVisible = true;
    },
    onWriteReview: function(form) {
      this.$store.dispatch('writeReview', {
        form,
        movieId: this.$route.params.id,
      });

      form = {
        content: '',
        score: 0.0,
      };
    },
  },
  components: {
    ReviewModal,
    MovieReview,
  },
  created: function() {
    this.$store.dispatch('getReviews', this.$route.params.id);
  },
};
</script>

<style lang="scss" scoped>
.movie_reviews {
  margin: 0 auto;
  max-width: 1200px;
  padding: 50px 0;
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

  .summary {
    align-items: center;
    border-bottom: 1px solid rgba(0, 0, 0, 0.2);
    display: flex;
    padding: 0 0 10px 10px;

    i {
      color: #ffda77;
      font-size: 1rem;
      margin-right: 5px;
    }
  }

  .write_review {
    align-items: center;
    display: flex;
    justify-content: flex-end;
    padding: 20px 0;

    .suggestion {
      font-size: 0.9rem;
      margin-right: 10px;

      strong {
        color: #1fab89;
      }
    }

    .write_button {
      all: unset;
      border: 2px solid #1fab89;
      border-radius: 4px;
      color: #595959;
      cursor: pointer;
      font-size: 0.9rem;
      padding: 5px 10px;

      i {
        font-size: 1rem;
        margin-right: 5px;
      }
    }
  }

  .reviews {
    margin-top: 20px;
  }
}
</style>
