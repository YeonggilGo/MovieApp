<template>
  <div class="modal_container" v-if="isVisible" @click.self="$emit('close')">
    <div class="review_modal" ref="reviewModal">
      <h1 class="title">리뷰 작성</h1>

      <div class="content_input">
        <input
          type="text"
          maxlength="30"
          class="content"
          v-model="form.content"
        />
        <div
          for="content"
          class="content_label"
          :class="{ writed: form.content.length > 0 }"
          aria-hidden="true"
        >
          내용
        </div>
      </div>

      <div class="rating_input">
        <h5 class="rating_title">평점</h5>
        <star-rating
          v-model="form.score"
          :max-rating="10"
          :star-size="20"
          text-class="rating_text"
        />
      </div>

      <div class="buttons">
        <button class="submit_button" @click="() => onSubmit(form)">
          작성
        </button>
        <button class="cancel_button" @click="$emit('close')">취소</button>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating';

export default {
  name: 'ReviewModal',
  components: {
    StarRating,
  },
  data: function() {
    return {
      form: {
        content: '',
        score: 0,
      },
    };
  },
  methods: {
    onClickOutsideModal: function(e) {
      if (!this.$refs.reviewModal.contains(e.target)) {
        this.$emit('invisible');
      }
    },
  },
  props: {
    isVisible: Boolean,
    initialForm: Object,
    onSubmit: Function,
  },
  created: function() {
    if (this.initialForm) {
      this.form = this.initialForm;
    }
  },
};
</script>

<style lang="scss">
.modal_container {
  align-items: center;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  height: 100%;
  justify-content: center;
  left: 0;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;

  .review_modal {
    background: #fff;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    max-width: 560px;
    padding: 30px;
    width: 100%;

    .title {
      font-size: 1.2rem;
      margin-bottom: 30px;
    }

    .content_input {
      margin-bottom: 30px;
      position: relative;

      &:focus-within .content_label {
        color: #1fab89;
        left: -2px;
        top: -20px;
        transform: scale(0.75);
      }

      &:not(:focus-within) .writed {
        color: #595959;
        left: -2px;
        top: -20px;
        transform: scale(0.75);
      }

      .content {
        border: none;
        border-bottom: 2px solid #595959;
        color: #595959;
        padding: 5px 0;
        width: 100%;

        &:focus {
          border-bottom: 2px solid #1fab89;
          outline: none;
        }
      }

      .content_label {
        color: #595959;
        left: 0;
        pointer-events: none;
        position: absolute;
        top: 5px;
        transition: 0.15s cubic-bezier(0.4, 0, 0.2, 1);
      }
    }

    .rating_input {
      margin-bottom: 30px;

      .rating_title {
        color: #595959;
        font-weight: normal;
        margin-bottom: 5px;
      }

      .rating_text {
        border: 1px solid #cfcfcf;
        border-radius: 5px;
        color: #999;
        font-size: 1rem;
        font-weight: bold;
        padding: 0 5px;
      }
    }

    .buttons {
      .submit_button,
      .cancel_button {
        all: unset;
        border-radius: 4px;
        color: #fff;
        cursor: pointer;
        font-size: 0.9rem;
        padding: 4px 20px;
        margin-right: 15px;
      }

      .submit_button {
        background: #1fab89;
      }

      .cancel_button {
        background: #595959;
      }
    }
  }
}
</style>
