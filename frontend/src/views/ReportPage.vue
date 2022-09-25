<template>
    <div class="bg-gray-100">
        <div class=" h-screen shadow-inner">
            <Navbar></Navbar>
            <div class="px-64">
                <div class="bg-opacity-10 backdrop-blur bg-white h-screen shadow-2xl">
                    <div class="grid grid-cols-1">
            <!-- Snippet -->
            <div class="flex justify-center text-gray-600">
              <div class="w-3/4 p-4 sm:px-6">
                <!-- Chart widget -->
                <div
                  class="flex w-full flex-col col-span-full xl:col-span-8 bg-white shadow-lg rounded-sm border border-gray-200">
                  <header class="px-5 py-4 border-b border-gray-300 items-center">
                    <h2 class="font-bold text-3xl text-gray-800 text-center font-rale tracking-widest">Общее описание
                      логов</h2>
                  </header>
                  <div class="flex justify-center px-1 py-2 ml-16">
                    <div class="flex">
                      <!-- Unique Visitors -->
                      <div class="flex items-center py-2 mr-6">
                        <div class="mr-1">
                          <div class="flex items-center justify-center">
                            <div class="text-3xl font-bold text-gray-800 mr-2">{{this.sum_into}}</div>
                          </div>
                          <div class="text-lg text-gray-500 font-corme">Общее количество JOIN</div>
                        </div>
                      </div>
                      <!-- Total Pageviews -->
                      <div class="flex items-center py-2 mr-6">
                        <div class="mr-1">
                          <div class="flex items-center justify-center">
                            <div class="text-3xl font-bold text-gray-800 mr-2">{{this.sum_froms}}</div>
                          </div>
                          <div class="text-lg text-gray-500 font-corme">Общее количество FROM</div>
                        </div>
                      </div>
                      <!-- Bounce Rate -->
                      <div class="flex items-center py-2">
                        <div class="mr-5">
                          <div class="flex items-center justify-center">
                            <div class="text-3xl font-bold text-gray-800 mr-2">{{this.sum_into}}</div>
                            <div class="text-sm font-medium text-yellow-500"></div>
                          </div>
                          <div class="text-lg text-gray-500 font-corme">Общее количество INTO</div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- Chart built with Chart.js 3 -->
                  <div class="flex justify-start mb-3 ml-12">
                    <Scatter :chart-options="chartOptions" :chart-data="chartData" :chart-id="chartId"
                      :dataset-id-key="datasetIdKey" :plugins="plugins" :css-classes="cssClasses" :styles="styles"
                      :width="width" :height="height" />
                    <div class="container">
                      <div class="flex justify-center mt-32">
                        <p class="font-semibold text-xl font-corme tracking-widest">Самая востребованная таблица</p>
                      </div>
                      <div class="flex justify-center">
                        <p class="font-semibold text-6xl font-rale tracking-widest ">{{this.most_wanted_name}}</p>
                        <p class="font-italic text-1xl font-rale tracking-widest ">{{this.most_wanted_count}} обращений
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
                </div>
            </div>
            
        </div>
    </div>
</div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import axios from 'axios'
import { Scatter } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  PointElement,
  LinearScale
} from 'chart.js'
ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  PointElement,
  LinearScale
)
export default {
    components: { Navbar, Scatter },
    props: {
    chartId: {
      type: String,
      default: 'scatter-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 400
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => { }
    },
    plugins: {
      type: Array,
      default: () => []
    },
    into: {
      type: Array,
      default: () => []
    },
    join: {
      type: Array,
      default: () => []
    },
    from: {
      type: Array,
      default: () => []
    },
  },
  data() {
    return {
      sum_into: '',
      sum_joins: '',
      sum_froms: '',
      most_wanted_count: '',
      most_wanted_name: '',
      chartData: {
        datasets: [
          {
            label: 'JOIN',
            fill: false,
            borderColor: '#887BB5',
            backgroundColor: '#4528A4',
            data: [this.join]

          },
          {
            label: 'INTO',
            fill: false,
            borderColor: '#f87979',
            backgroundColor: '#FF3F3F',
            data: [this.into]
          },
          {
            label: 'FROM',
            fill: false,
            borderColor: '#23D323',
            backgroundColor: '#23D323',
            data: [this.from]
          }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        }
      }
    },
  mounted(){axios.get('http://127.0.0.1:8000/main/report/').then(response => {
    this.$data.chartData.datasets[0].data = response.data.join
        this.$data.chartData.datasets[1].data = response.data.into
        this.$data.chartData.datasets[2].data = response.data.from
        this.sum_into = response.data.sum_into
        this.sum_joins = response.data.sum_joins
        this.sum_froms = response.data.sum_froms
        this.most_wanted_count = response.data.most_wanted.count
        this.most_wanted_name = response.data.most_wanted.table
        console.log(this.$data.chartData.datasets[1].data )

  })}
}
</script>

<style>

</style>