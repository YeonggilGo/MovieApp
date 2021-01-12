<template>
  <div class="post_detail_container">
    <div class="post_detail_inner">
      <div class="header">
        <h1 class="title">{{ post.title }}</h1>
        <div class="buttons" v-if="username === post.username">
          <router-link
            class="update_button"
            :to="{ name: 'UpdatePost', params: { id: post.id } }"
          >
            수정
          </router-link>
          <button type="button" class="delete_button" @click="onDelete">
            삭제
          </button>
        </div>
      </div>
      <div class="infos">
        <div class="info">글쓴이 : {{ post.username }}</div>
        <div class="info">작성 시각 : {{ post.created_at }}</div>
        <div class="info">수정 시각 : {{ post.updated_at }}</div>
      </div>
      <div class="content" v-html="post.content" />
      <div class="comment_title"><span class="first_letter">C</span>OMMENT</div>
      <div class="comment_form">
        <input
          type="text"
          class="comment_input"
          v-model.trim="commentContent"
        />
        <button type="button" class="submit_button" @click="onWriteComment">
          작성
        </button>
      </div>
      <comments />
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import moment from 'moment';

import Comments from '../components/community/Comments.vue';

export default {
  name: 'PostDetail',
  data: function() {
    return {
      commentContent: '',
    };
  },
  components: {
    Comments,
  },
  computed: {
    ...mapState({
      post: state => ({
        ...state.community.post,
        created_at: moment(state.community.post.created_at).format(
          'YYYY년 M월 D일 H시 M분 S초'
        ),
        updated_at: moment(state.community.post.updated_at).format(
          'YYYY년 M월 D일 H시 M분 S초'
        ),
      }),
      isLoggedIn: state => state.user.isLoggedIn,
      username: state => state.user.username,
    }),
  },
  created: function() {
    if (!this.isLoggedIn) {
      alert('로그인이 필요한 서비스입니다.');
      return this.$router.push('/login');
    }

    this.$store.dispatch('getPost', this.$route.params.id);
    this.$store.dispatch('getComments', this.$route.params.id);
  },
  methods: {
    onDelete: function() {
      const willDelete = confirm('정말 삭제하시겠습니까?');

      if (willDelete) {
        this.$store.dispatch('deletePost', this.post.id);
      }
    },
    onWriteComment: function() {
      if (this.commentContent.length > 0) {
        this.$store.dispatch('writeComment', {
          content: this.commentContent,
          postId: this.$route.params.id,
        });
        this.commentContent = '';
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.post_detail_container {
  padding: 50px 0;

  .post_detail_inner {
    margin: 0 auto;
    max-width: 1200px;
    width: 100%;

    .header {
      align-items: flex-end;
      border-bottom: 1px solid #e9e9e9;
      display: flex;
      justify-content: space-between;
      margin-bottom: 15px;
      padding-bottom: 10px;

      .title {
        font-size: 2rem;
        font-weight: bold;
      }

      .buttons {
        align-items: center;
        display: flex;

        .update_button {
          margin-right: 10px;
        }

        .delete_button {
          all: unset;
          cursor: pointer;
        }

        .update_button,
        .delete_button {
          color: #595959;
          font-size: 0.9rem;
        }
      }
    }

    .infos {
      margin-bottom: 30px;

      .info {
        color: #595959;
        font-size: 0.8rem;
      }
    }

    .content {
      border-bottom: 1px solid #e9e9e9;
      min-height: 300px;
      padding-bottom: 15px;
    }

    .comment_title {
      color: #1fab89;
      font-size: 1.4rem;
      font-weight: bold;
      margin-top: 40px;

      .first_letter {
        background: #1fab89;
        color: #fff;
        display: inline-block;
        padding: 0 5px;
      }
    }

    .comment_form {
      align-items: center;
      display: flex;
      margin-top: 20px;

      .comment_input {
        margin-right: 10px;
        max-width: 560px;
        padding: 2px 0;
        text-indent: 5px;
        width: 100%;
      }

      .submit_button {
        all: unset;
        background: #1fab89;
        border-radius: 4px;
        color: #fff;
        cursor: pointer;
        font-size: 0.9rem;
        padding: 5px 20px;
      }
    }
  }
}
</style>
