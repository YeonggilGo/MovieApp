<template>
  <div class="comments" v-if="comments.length > 0">
    <div class="comment" :key="comment.id" v-for="comment in comments">
      <div class="header">
        <div class="username">{{ comment.username }}</div>
        <div class="created_at">작성 시각 : {{ comment.created_at }}</div>
        <div class="updated_at">수정 시각 : {{ comment.updated_at }}</div>
      </div>
      <div class="main">
        <div class="content">{{ comment.content }}</div>
        <button
          class="delete_button"
          v-if="$store.state.user.username === comment.username"
          @click="() => onClickDeleteButton(comment)"
        >
          <i class="far fa-times-circle"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import moment from 'moment';

export default {
  name: 'Comments',
  computed: {
    ...mapState({
      comments: state =>
        state.community.comments.map(comment => ({
          ...comment,
          created_at: moment(comment.created_at).format(
            'YYYY년 M월 D일 H시 m분 s초'
          ),
          updated_at: moment(comment.updated_at).format(
            'YYYY년 M월 D일 H시 m분 s초'
          ),
        })),
    }),
  },
  methods: {
    onClickDeleteButton: function(comment) {
      const willDelete = confirm('정말 삭제하시겠습니까?');

      if (willDelete) {
        this.$store.dispatch('deleteComment', comment.id);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.comments {
  margin-top: 30px;

  .comment {
    & + .comment {
      margin-top: 20px;
    }

    .header {
      align-items: center;
      display: flex;
      margin-bottom: 5px;

      .username {
        font-size: 1rem;
        font-weight: bold;
        margin-right: 30px;
      }

      .created_at,
      .updated_at {
        color: #595959;
        font-size: 0.7rem;
      }

      .created_at {
        margin-right: 20px;
      }
    }

    .main {
      align-items: center;
      display: flex;

      .content {
        font-size: 0.8rem;
      }

      .delete_button {
        all: unset;
        cursor: pointer;
        margin-left: 10px;

        i {
          color: #ff0000;
          font-size: 0.9rem;
        }
      }
    }
  }
}
</style>
