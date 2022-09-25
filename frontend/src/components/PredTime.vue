<template>
  <div v-if="loading" key="loading">
    <div class="text-center">
      <div class="spinner-border" role="status" style="width: 3rem; height: 3rem;">
        <span class="visually-hidden">Загрузка...</span>
      </div>
    </div>
  </div>
  <div v-else-if="M1" key="M1.probs">Предсказание выполнения запроса по количеству операторов: {{M1.data.result}} ms</div>
  <div v-else-if="M2" key="M2.data">Предсказание выполнения запроса по количеству операторов: {{M2.data.result}} ms</div>
  <div v-else-if="M3" key="M3.compl">Предсказание выполнения запроса по количеству операторов: {{M3.data.result}} ms</div>
  <div v-else key="not-found">Не найдено</div>
</template>

<script>
import { mapState } from 'vuex';
export default {
  computed: mapState(['loading', 'M1', 'M2', 'M3']),
};
</script>

<style>

</style>