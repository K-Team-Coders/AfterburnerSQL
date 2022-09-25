<template>
  <div class="">
    <Navbar></Navbar>
    <div class="h-auto bg-gradient-to-r from-cyan-500 to-pink-500">
      <div class="px-64">
        <div class="bg-opacity-25 backdrop-blur bg-white/30 rounded shadow-2xl ">
          <div class="flex justify-center">
            <form class="flex bg-white items-center mr-12 mt-12">
              <label class="block">
                <input accept=".csv" type="file" class="block w-full text-xl mr-52 font-rale text-slate-500
                     file:mr-0 file:py-4 file:px-10
                     file:border-0
                     file:text-xl file:font-semibold
                     file:bg-violet-100 file:text-violet-700
                     hover:file:bg-pink-200
                     " ref="file" v-on:change="handleFileUpload()" />
              </label>
              <button
                class="ml-32 font-rale bg-violet-50 hover:bg-green-200 text-violet-700 text-xl font-semibold  py-3 px-7"
                @click="submitFile()">
                Загрузить
              </button>
            </form>
          </div>
          <div class="grid grid-cols-3 col-auto mr-12 mt-12">
            <div class="max-w-sm w-full lg:max-w-full lg:flex">
              <div
                class="h-48 lg:h-auto lg:w-12 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden">
              </div>
              <div
                class="border-r border-b border-l w-full shadow-xl hover:shadow-2xl border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
                <div class="mb-8">
                  <div iv class="text-gray-900 font-bold text-3xl mb-2 font-corme text-center">Подсчет запросов к
                    таблицам</div>
                  <p class="text-gray-700 text-xl font-rale text-center">Позволяет проанализировать общее количество
                    запросов к таблице.</p>
                </div>
              </div>
            </div>
            <div class="max-w-sm w-full lg:max-w-full lg:flex">
              <div
                class="h-48 lg:h-auto lg:w-12 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden">
              </div>
              <div
                class="border-r border-b border-l w-full shadow-xl hover:shadow-2xl border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
                <div class="mb-8">
                  <div  class="text-gray-900 font-bold text-3xl mb-2 font-corme text-center">Подсчет по запросам от
                    разработчиков</div>
                  <p class="text-gray-700 text-xl font-rale text-center">Позволяет выявить наиболее активных
                    разработчиков, и тех кто единожды загрузил данные</p>
                </div>
              </div>
            </div>
            <div class="max-w-sm w-full lg:max-w-full lg:flex">
              <div
                class="h-48 lg:h-auto lg:w-12 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden">
              </div>
              <div
                class="border-r border-b border-l w-full shadow-xl hover:shadow-2xl border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
                <div class="mb-8">
                  <div iv class="text-gray-900 font-bold text-3xl mb-2 font-corme text-center">Предсказание времени выполнения SQL запроса на основе тела запроса</div>
                  <p class="text-gray-700 text-xl font-rale text-center">Предсказание проводится на основе моделей машинного обучения и нейоронных сетей: <ul><li>1) Модель регрессии.</li><li>2) Дерево решений</li></ul> </p>
                </div>
              </div>
            </div>
          </div>
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
    <div class=" bg-gradient-to-r from-cyan-500 to-pink-500">
      <div class="px-64">
        <div class="h-screen -mt-1 px-3 bg-opacity-25 backdrop-blur bg-white/30 rounded shadow-2xl">
          <div class="container w-3/4">
            <div class="flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden">
            </div>
            <div
              class="mt-4 border-r border-b border-l w-full mr-2 shadow-xl hover:shadow-2xl border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
              <div class="mb-8">
                <div class="text-gray-900 font-base text-3xl mb-2 font-rale text-center border-b ">
                  <p class="border-b border-gray-300">Граф отношений пользователь-таблица-вид отношения</p>
                  <svg width="960" height="600" class="container-border"></svg>
                </div>
                <p class="text-gray-700 text-xl font-rale text-center"></p>
              </div>
            </div>
            <div class="flex justify-center py-3">
              <Search></Search>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Search from '../components/Search.vue'
import * as d3 from 'd3'
import Navbar from '../components/Navbar.vue';
import BarChart from '../components/charts/BarChart.vue';
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

  components: { Navbar, Scatter, Search },
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
  methods:
  {
    submitFile() {
      let formData = new FormData();
      formData.append('file', this.file);
      axios.post('http://127.0.0.1:8000/main/load_file_tables/',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      ).then(response => {
        this.$data.chartData.datasets[0].data = response.data.join
        this.$data.chartData.datasets[1].data = response.data.into
        this.$data.chartData.datasets[2].data = response.data.from
        this.sum_into = response.data.sum_into
        this.sum_joins = response.data.sum_joins
        this.sum_froms = response.data.sum_froms
        this.most_wanted_count = response.data.most_wanted.count
        this.most_wanted_name = response.data.most_wanted.table

        axios.post('http://127.0.0.1:8000/main/load_file_users/',
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }).then(response => {
            let nodes2 = response.data.nodes1234
            console.log(nodes2)
            let edges = response.data.edges1234
            console.log(edges)
            let marge = { top: 60, bottom: 60, left: 60, right: 60 }
            let svg = d3.select('svg')
            let width = svg.attr('width')
            let height = svg.attr('height')
            let g = svg.append('g')
              .attr('transform', 'translate(' + marge.top + ',' + marge.left + ')')
            // Node Dataset
            // Side Dataset
            // 边集
            // Set a color scale
            // 设置一个颜色比例尺
            let colorScale = d3.scaleOrdinal()
              .domain(d3.range(nodes2.length))
              .range(d3.schemeCategory10)
            // Create a new force guide diagram
            // 新建一个力导向图
            let forceSimulation = d3.forceSimulation()
              .force('link', d3.forceLink())
              .force('charge', d3.forceManyBody())
              .force('center', d3.forceCenter())
            // Generate node data
            // 生成节点数据
            forceSimulation.nodes(nodes2)
              .on('tick', ticked)
            // Generate side data
            // 生成边数据
            forceSimulation.force('link')
              .links(edges)
              .distance(function (d) { // side length / 每一边的长度
                return d.value * 100
              })
            // Set drawing center location

            forceSimulation.force('center')
              .x(width / 2)
              .y(height / 2)
            // Draw side

            let links = g.append('g')
              .selectAll('line')
              .data(edges)
              .enter()
              .append('line')
              .attr('stroke', function (d, i) {
                return colorScale(i)
              })
              .attr('stroke-width', 1)
            // Text on side

            let linksText = g.append('g')
              .selectAll('text')
              .data(edges)
              .enter()
              .append('text')
              .text(function (d) {
                return d.relation
              })
            // Create group

            let gs = g.selectAll('.circleText')
              .data(nodes2)
              .enter()
              .append('g')
              .attr('transform', function (d) {
                let cirX = d.x
                let cirY = d.y
                return 'translate(' + cirX + ',' + cirY + ')'
              })
              .call(d3.drag()
                .on('start', started)
                .on('drag', dragged)
                .on('end', ended)
              )
            // Draw node

            gs.append('circle')
              .attr('r', 10)
              .attr('fill', function (d, i) {
                return colorScale(i)
              })
            // Draw text

            gs.append('text')
              .attr('x', -10)
              .attr('y', -20)
              .attr('dy', 10)
              .text(function (d) {
                return d.name
              })
            // ticked
            function ticked() {
              links
                .attr('x1', function (d) { return d.source.x })
                .attr('y1', function (d) { return d.source.y })
                .attr('x2', function (d) { return d.target.x })
                .attr('y2', function (d) { return d.target.y })
              linksText
                .attr('x', function (d) { return (d.source.x + d.target.x) / 2 })
                .attr('y', function (d) { return (d.source.y + d.target.y) / 2 })
              gs
                .attr('transform', function (d) { return 'translate(' + d.x + ',' + d.y + ')' })
            }
            // drag
            function started(d) {
              if (!d3.event.active) {
                forceSimulation.alphaTarget(0.8).restart() // Set the attenuation coefficient to simulate the node position movement process. The higher the value, the faster the movement. The value range is [0, 1] // 设置衰减系数，对节点位置移动过程的模拟，数值越高移动越快，数值范围[0, 1]
              }
              d.fx = d.x
              d.fy = d.y
            }
            function dragged(d) {
              d.fx = d3.event.x
              d.fy = d3.event.y
            }
            function ended(d) {
              if (!d3.event.active) {
                forceSimulation.alphaTarget(0)
              }
              d.fx = null
              d.fy = null
            }
          })
      })
    },
    handleFileUpload() {
          this.file = this.$refs.file.files[0]
        }
  }
}
</script>

<style>
.filearea {
  background-image: linear-gradient(to right,
      #49005c,
      #0f0061 50%,
      rgb(255, 255, 255) 50%);
  background-size: 200% 100%;
  background-position: -100%;
  display: inline-block;
  padding: 5px 0;
  position: relative;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: all 0.3s ease-in-out;
}

.filearea:before {
  content: '';
  background: #22033f;
  display: block;
  position: absolute;
  bottom: -3px;
  left: 0;
  width: 0;
  height: 3px;
  transition: all 0.3s ease-in-out;
}

.filearea:hover {
  background-position: 0;
}

.filearea:hover::before {
  width: 100%;
}

.filearea {
  display: grid;
  font-family: 'Poppins', sans-serif;
  font-size: 27px;
  font-weight: 700;
  place-items: center;
}
</style>
