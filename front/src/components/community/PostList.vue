<template>
  <table class="post_list">
    <thead>
      <tr>
        <th class="index">번호</th>
        <th class="title">제목</th>
        <th class="author">글쓴이</th>
      </tr>
    </thead>
    <tbody>
      <tr
        class="post"
        :key="post.id"
        v-for="post in $store.state.community.posts"
      >
        <td class="index">{{ post.id }}</td>
        <td class="title">
          <router-link :to="{ name: 'PostDetail', params: { id: post.id } }">
            {{ post.title }}
          </router-link>
        </td>
        <td class="author">{{ post.username }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'PostList',
  created: function() {
    this.$store.dispatch('getPosts', this.$route.query.page);
  },
  computed: {
    page: function() {
      return this.$route.query.page;
    },
  },
  watch: {
    page: function() {
      this.$store.dispatch('getPosts', this.page);
    },
  },
};
</script>

<style lang="scss" scoped>
.post_list {
  border-collapse: collapse;
  width: 100%;

  thead {
    background: #f9f9f9;

    th {
      border-bottom: 1px solid #e6e9e9;
      border-top: 1px solid #ccc;
      color: #595959;
      font-size: 0.8rem;
      padding: 2px 0;

      &.title {
        width: 80%;
      }
    }
  }

  tbody {
    tr {
      &:hover {
        background: #f9f9f9;
      }

      td {
        border-bottom: 1px solid #e6e9e9;
        padding: 10px 10px;
        text-align: center;

        &.title {
          font-size: 0.9rem;
        }

        &.author {
          font-size: 0.8rem;
        }
      }
    }
  }
}
</style>
