<template>
  <div class="write_form">
    <label for="title">제목</label>
    <input id="title" class="title" type="text" v-model="title" />

    <label for="content">내용</label>
    <textarea id="content" class="content" rows="20" v-model="content" />

    <button class="submit_button" @click="() => onSubmit({ title, content })">
      작성하기
    </button>
  </div>
</template>

<script>
export default {
  name: 'WriteForm',
  data: function() {
    return {
      title: '',
      content: '',
    };
  },
  props: {
    initialValue: {
      type: Object || null,
      default: null,
    },
    onSubmit: Function,
  },
  watch: {
    initialValue: function() {
      const isEmpty = JSON.stringify(this.initialValue) === '{}';

      if (!isEmpty) {
        this.title = this.initialValue.title;
        this.content = this.initialValue.content;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.write_form {
  display: flex;
  flex-direction: column;

  * {
    font-size: 1rem;
  }

  label {
    margin-bottom: 10px;
  }

  .title {
    margin-bottom: 20px;
    padding: 5px;
  }

  .content {
    margin-bottom: 30px;
    padding: 10px;
    resize: none;
  }

  .submit_button {
    all: unset;
    background: #1fab89;
    color: #fff;
    cursor: pointer;
    font-size: 0.9rem;
    padding: 10px 20px;
    text-align: center;
  }
}
</style>
