<template>
  <div class="update_post_container">
    <div class="update_post_inner">
      <h1 class="title">게시물 수정</h1>
      <write-form :initialValue="post" :onSubmit="onSubmit" />
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import axiosClient from '../lib/axiosClient';

import WriteForm from '../components/community/WriteForm.vue';

export default {
  name: 'UpdatePost',
  data: function() {
    return {
      post: {},
    };
  },
  computed: {
    ...mapState({
      isLoggedIn: state => state.user.isLoggedIn,
    }),
  },
  methods: {
    onSubmit: function(form) {
      this.$store.dispatch('updatePost', {
        form,
        postId: this.$route.params.id,
      });
    },
  },
  created: function() {
    if (!this.isLoggedIn) {
      alert('로그인이 필요한 서비스입니다.');
      return this.$router.push('/login');
    }

    axiosClient
      .get(`/community/${this.$route.params.id}/detail`, {
        headers: {
          Authorization: `JWT ${this.$store.state.user.token}`,
        },
      })
      .then(res => {
        if (res.data.username !== this.$store.state.user.username) {
          alert('잘못된 접근입니다.');
          return this.$router.push('/');
        }
        this.post = res.data;
      })
      .catch(e => console.error(e));
  },
  components: {
    WriteForm,
  },
};
</script>

<style lang="scss" scoped>
.update_post_container {
  padding: 30px 0 50px;

  .update_post_inner {
    margin: 0 auto;
    max-width: 1200px;
    width: 100%;

    .title {
      font-size: 1.8rem;
      font-weight: normal;
      margin-bottom: 30px;
    }
  }
}
</style>
