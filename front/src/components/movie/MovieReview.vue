<template>
  <div class="review">
    <div class="username">{{ review.username }}</div>
    <div class="rating"><i class="fas fa-star"></i> {{ review.score }}</div>
    <div class="content">{{ review.content }}</div>
    <div class="buttons" v-if="$store.state.user.username === review.username">
      <button type="button" class="update_button" @click="onClickUpdateButton">
        수정
      </button>
      <button type="button" class="delete_button" @click="onDeleteReview">
        삭제
      </button>
    </div>

    <review-modal
      :isVisible="isModalVisible"
      :initialForm="{ content: review.content, score: review.score }"
      :onSubmit="onUpdateReview"
      @close="isModalVisible = false"
    />
  </div>
</template>

<script>
import ReviewModal from './ReviewModal.vue';
export default {
  name: 'MovieReview',
  data: function() {
    return {
      isModalVisible: false,
    };
  },
  props: {
    review: Object,
  },
  methods: {
    onClickUpdateButton: function() {
      this.isModalVisible = true;
    },
    onUpdateReview: function(form) {
      this.$store.dispatch('updateReview', {
        form,
        movieId: this.$route.params.id,
        reviewId: this.review.id,
      });

      this.isModalVisible = false;
    },
    onDeleteReview: function() {
      const willDelete = confirm('정말 삭제하시겠습니까?');

      if (willDelete) {
        this.$store.dispatch('deleteReview', {
          movieId: this.$route.params.id,
          reviewId: this.review.id,
        });
      }
    },
  },
  components: {
    ReviewModal,
  },
};
</script>

<style lang="scss" scoped>
.review {
  align-items: center;
  background: #f5f5f5;
  border-radius: 10px;
  display: flex;
  padding: 20px 30px;

  & + .review {
    margin-top: 20px;
  }

  .username {
    color: #595959;
    font-size: 0.9rem;
    width: 100px;
  }

  .rating {
    align-items: center;
    color: #1fab89;
    display: flex;
    font-weight: bold;
    width: 70px;

    i {
      color: #ffda77;
      font-size: 0.7rem;
      margin-right: 5px;
    }
  }

  .content {
    font-size: 0.9rem;
  }

  .buttons {
    margin-left: auto;

    .update_button,
    .delete_button {
      all: unset;
      color: #595959;
      cursor: pointer;
      font-size: 0.8rem;
    }

    .update_button {
      margin-right: 10px;
    }
  }
}
</style>
