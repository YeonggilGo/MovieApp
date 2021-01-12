<template>
  <footer class="footer">
    <div class="footer_inner">
      <div class="brand_logo">GLORYBOX</div>
      <div class="copyright">&copy; copyright 고영길 & 안광훈</div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
};
</script>

<style lang="scss" scope>
.footer {
  align-items: center;
  background: #212121;
  color: #b0b2b0;
  display: flex;
  padding: 50px 0;
  width: 100%;

  .footer_inner {
    align-items: center;
    display: flex;
    margin: 0 auto;
    max-width: 1200px;
    width: 100%;

    .brand_logo {
      margin-right: 50px;
    }
  }
}
</style>
