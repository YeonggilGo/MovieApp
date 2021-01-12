<template>
  <div class="pagination_container">
    <router-link
      :to="{ name: routeName, query: { page: currentPage - 1 } }"
      class="pagination_button pagination_icon"
      :class="{ disabled: currentPage === 1 }"
    >
      <i class="fas fa-angle-left"></i>
    </router-link>

    <router-link
      :to="{ name: routeName, query: { page: page + firstPage - 1 } }"
      class="pagination_button"
      :class="{ active: page + firstPage - 1 === currentPage }"
      :key="page"
      v-for="page in Math.min(10, totalPage - firstPage + 1)"
    >
      {{ page + firstPage - 1 }}
    </router-link>

    <router-link
      :to="{ name: routeName, query: { page: currentPage + 1 } }"
      class="pagination_button pagination_icon"
      :class="{ disabled: currentPage === totalPage }"
    >
      <i class="fas fa-angle-right"></i>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'Pagination',
  props: {
    totalPage: Number,
    routeName: String,
  },
  computed: {
    currentPage: function() {
      return Number(this.$route.query.page);
    },
    firstPage: function() {
      return (Math.ceil(Number(this.$route.query.page) / 10, 10) - 1) * 10 + 1;
    },
  },
};
</script>

<style lang="scss" scoped>
.pagination_container {
  align-items: center;
  display: flex;
  justify-content: center;

  .pagination_button {
    align-items: center;
    display: flex;
    height: 40px;
    justify-content: center;
    width: 40px;

    &.pagination_icon {
      border: 1px solid #ccc;
      color: #888;
      font-size: 1.2rem;

      &:first-child {
        margin-right: 15px;
      }

      &:last-child {
        margin-left: 15px;
      }

      &.disabled {
        pointer-events: none;
      }
    }

    &.active {
      border: 1px solid #000;
    }
  }
}
</style>
