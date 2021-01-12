<template>
  <div class="write_post_container">
    <div class="write_post_inner">
      <div class="title">글 작성</div>
      <write-form :onSubmit="onSubmit" />
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

import WriteForm from '../components/community/WriteForm.vue';

export default {
  name: 'WritePost',
  methods: {
    onSubmit: function(form) {
      this.$store.dispatch('writePost', form);
    },
  },
  components: {
    WriteForm,
  },
  computed: {
    ...mapState({
      isLoggedIn: state => state.user.isLoggedIn,
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
.write_post_container {
  padding: 30px 0 50px;

  .write_post_inner {
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
