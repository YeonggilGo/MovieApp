<template>
  <div
    class="carousel_item"
    :style="{
      background:
        'linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url(' +
        imageSrc +
        ') center center/cover',
    }"
  >
    <div class="item_inner">
      <h1 class="genre">{{ koreanGenre }}</h1>
      <router-link
        :to="{ name: 'Movies', params: { category: genre } }"
        class="more_info"
        >보러 가기</router-link
      >
    </div>
  </div>
</template>

<script>
import movieStatic from '../../assets/js/movie';

export default {
  name: 'MovieCarouselItem',
  props: {
    genre: String,
    imageSrc: String,
  },
  data: function() {
    return {
      koreanGenre: movieStatic.category[this.genre],
    };
  },
};
</script>

<style lang="scss" scoped>
.carousel_item {
  height: 700px;
  position: relative;

  .item_inner {
    align-items: center;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: center;
    margin: 0 auto;
    max-width: 1200px;
    position: relative;
    width: 100%;

    .genre {
      color: #fff;
      font-size: 4rem;
      margin-bottom: 10px;
    }

    .more_info {
      all: unset;
      background: #f43748;
      border-radius: 4px;
      color: #fff;
      cursor: pointer;
      padding: 10px 40px;
    }
  }
}
</style>
