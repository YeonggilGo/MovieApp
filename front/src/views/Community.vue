<template>
  <div class="community_container">
    <div class="community_inner">
      <div class="title">자유게시판</div>
      <post-list />
      <div class="write_button_wrapper">
        <router-link :to="{ name: 'WritePost' }" class="write_button">
          글쓰기
        </router-link>
      </div>
      <pagination
        :totalPage="Math.ceil(totalPosts / 10)"
        :routeName="'Community'"
      />
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

import Pagination from '../components/common/Pagination.vue';
import PostList from '../components/community/PostList.vue';

export default {
  name: 'Community',
  components: {
    PostList,
    Pagination,
  },
  computed: {
    ...mapState({
      isLoggedIn: state => state.user.isLoggedIn,
      totalPosts: state => state.community.totalPosts,
    }),
  },
  created: function() {
    if (!this.isLoggedIn) {
      alert('로그인이 필요한 서비스입니다.');
      this.$router.push('/login');
    }
  },
};
</script>

<style lang="scss" scoped>
.community_container {
  padding: 30px 0;

  .community_inner {
    margin: 0 auto;
    max-width: 1200px;
    width: 100%;

    .title {
      font-size: 1.8rem;
      font-weight: normal;
      margin-bottom: 30px;
    }

    .write_button_wrapper {
      margin: 30px 0;
      text-align: right;

      .write_button {
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
