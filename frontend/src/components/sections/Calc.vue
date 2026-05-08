<template>
  <section class="calc-section">

    <div class="calc-layout">

      <!-- LEFT -->
      <aside class="calc-left">

        <div class="calc-label">
          <span></span>
          калькулятор
        </div>

        <h1 class="calc-title">
          РАССЧИТАЕМ
          <br />
          СТОИМОСТЬ
          <br />
          <span>ВАШЕГО ПРОЕКТА</span>
        </h1>

        <p class="calc-description">
          Соберите digital-вкладку под ваш бизнес
          и получите предварительную оценку проекта.
        </p>

        <div class="calc-visual">

          <div class="folder folder-back"></div>
          <div class="folder folder-middle"></div>

          <div class="folder folder-front">

            <div class="folder-number">
              01
            </div>

            <div class="folder-name">
              launch
            </div>

            <div class="folder-lights">
              <span></span>
              <span></span>
            </div>

          </div>

        </div>

        <div class="left-features">

          <div class="left-feature">
            <strong>1–2 минуты</strong>
            <span>предварительный расчёт</span>
          </div>

          <div class="left-feature">
            <strong>Точная оценка</strong>
            <span>под задачи проекта</span>
          </div>

          <div class="left-feature">
            <strong>Без спама</strong>
            <span>только связь по проекту</span>
          </div>

        </div>

      </aside>

      <!-- RIGHT -->
      <div class="calc-right">

        <!-- PROJECTS -->
        <div class="calc-block">

          <div class="block-head">

            <div class="block-title">
              <span>01</span>
              ВЫБЕРИТЕ ТИП ПРОЕКТА
            </div>

            <div class="block-step">
              шаг 1 / 3
            </div>

          </div>

          <div class="project-grid">

            <button
              v-for="project in projects"
              :key="project.id"
              class="project-card"
              :class="{ active: selectedProject === project.id }"
              @click="selectedProject = project.id"
            >

              <div class="project-icon">
                {{ project.icon }}
              </div>

              <div class="project-content">

                <h4>
                  {{ project.title }}
                </h4>

                <p>
                  {{ project.description }}
                </p>

                <div class="project-start-price">
                  от {{ project.basePrice.toLocaleString('ru-RU') }} ₽
                </div>

              </div>

            </button>

          </div>

        </div>

        <!-- CMS -->
        <div class="calc-block">

          <div class="block-head">

            <div class="block-title">
              <span>02</span>
              НУЖНА ЛИ АДМИН-ПАНЕЛЬ?
            </div>

            <div class="block-step">
              шаг 2 / 3
            </div>

          </div>

          <div class="admin-grid">

            <button
              v-for="cms in cmsOptions"
              :key="cms.id"
              class="admin-card"
              :class="{ active: selectedCMS === cms.id }"
              @click="selectedCMS = cms.id"
            >

              <span class="admin-name">
                {{ cms.label }}
              </span>

              <span
                v-if="cms.priceAdd"
                class="admin-price"
              >
                +{{ cms.priceAdd.toLocaleString('ru-RU') }} ₽
              </span>

            </button>

          </div>

        </div>

        <!-- OPTIONS -->
        <div class="calc-block">

          <div class="block-head">

            <div class="block-title">
              <span>03</span>
              ДОПОЛНИТЕЛЬНЫЕ ВОЗМОЖНОСТИ
            </div>

            <div class="block-step">
              шаг 3 / 3
            </div>

          </div>

          <div class="options-groups">

            <!-- продвижение -->
            <div class="options-group">

              <div class="group-title">
                Продвижение
              </div>

              <div class="options-grid">

                <div
                  v-for="option in marketingOptions"
                  :key="option.id"
                  class="option-row"
                >

                  <span class="option-name">
                    {{ option.label }}
                  </span>

                  <button
                    class="toggle"
                    :class="{ active: option.active }"
                    @click="option.active = !option.active"
                  >
                    <span class="toggle-lever"></span>
                  </button>

                </div>

              </div>

            </div>

            <!-- производительность -->
            <div class="options-group">

              <div class="group-title">
                Производительность
              </div>

              <div class="options-grid">

                <div
                  v-for="option in performanceOptions"
                  :key="option.id"
                  class="option-row"
                >

                  <span class="option-name">
                    {{ option.label }}
                  </span>

                  <button
                    class="toggle"
                    :class="{ active: option.active }"
                    @click="option.active = !option.active"
                  >
                    <span class="toggle-lever"></span>
                  </button>

                </div>

              </div>

            </div>

            <!-- визуал -->
            <div class="options-group">

              <div class="group-title">
                Визуал
              </div>

              <div class="options-grid">

                <div
                  v-for="option in visualOptions"
                  :key="option.id"
                  class="option-row"
                >

                  <span class="option-name">
                    {{ option.label }}
                  </span>

                  <button
                    class="toggle"
                    :class="{ active: option.active }"
                    @click="option.active = !option.active"
                  >
                    <span class="toggle-lever"></span>
                  </button>

                </div>

              </div>

            </div>

          </div>

        </div>

        <!-- RESULT -->
        <div class="result-box">

          <div class="result-left">

            <div class="summary-top">

              <div>

                <div class="summary-label">
                  КОНФИГУРАЦИЯ ПРОЕКТА
                </div>

                <h3>
                  {{ currentProject.title }}
                </h3>

              </div>

              <div class="summary-badges">

                <div class="summary-time">
                  ~ {{ estimatedTime }}
                </div>

                <div class="status-badge">
                  готов к запуску
                </div>

              </div>

            </div>

            <div class="summary-grid">

              <div class="summary-row">
                <span>Тип проекта</span>
                <strong>{{ currentProject.title }}</strong>
              </div>

              <div class="summary-row">
                <span>Админ-панель</span>
                <strong>{{ currentCMS.label }}</strong>
              </div>

              <div class="summary-row">
                <span>Активных опций</span>
                <strong>{{ activeOptions.length }}</strong>
              </div>

              <div class="summary-row">
                <span>Срок реализации</span>
                <strong>{{ estimatedTime }}</strong>
              </div>

            </div>

          </div>

          <div class="result-right">

            <div class="total-label">
              Предварительная стоимость
            </div>

            <div
              ref="priceRef"
              class="total-value"
            >
              {{ formattedPrice }} ₽
            </div>

            <div class="total-meta">
              Точная стоимость определяется
              после обсуждения проекта.
            </div>

            <button
              class="discuss-btn"
              @click="scrollToContact"
            >
              Обсудить проект
            </button>

          </div>

        </div>

      </div>

    </div>

  </section>
</template>

<script setup>
import {
  ref,
  reactive,
  computed,
  watch,
  nextTick,
  onMounted
} from 'vue'

import { gsap } from 'gsap'

const selectedProject = ref('landing')
const selectedCMS = ref('none')

const priceRef = ref(null)

const projects = [
  {
    id: 'concept',
    title: 'Концепт',
    description: 'UI, структура, верстка',
    icon: '◎',
    basePrice: 20000
  },
  {
    id: 'landing',
    title: 'Лендинг',
    description: 'Продающая страница с анимациями',
    icon: '▣',
    basePrice: 35000
  },
  {
    id: 'shop',
    title: 'Интернет-магазин',
    description: 'Каталог, фильтры и ecommerce',
    icon: '◌',
    basePrice: 80000
  }
]

const cmsOptions = [
  {
    id: 'none',
    label: 'Не нужна',
    priceAdd: 0
  },
  {
    id: 'wordpress',
    label: 'WordPress',
    priceAdd: 15000
  },
  {
    id: 'joomla',
    label: 'Joomla',
    priceAdd: 12000
  },
  {
    id: 'grav',
    label: 'Grav',
    priceAdd: 10000
  }
]

const options = reactive([
  {
    id: 1,
    group: 'marketing',
    label: 'Яндекс.Директ',
    active: false,
    priceAdd: 5000
  },
  {
    id: 2,
    group: 'marketing',
    label: 'SEO оптимизация',
    active: false,
    priceAdd: 5000
  },
  {
    id: 3,
    group: 'marketing',
    label: 'AEO оптимизация',
    active: false,
    priceAdd: 4000
  },
  {
    id: 4,
    group: 'performance',
    label: 'Кеширование',
    active: false,
    priceAdd: 1000
  },
  {
    id: 5,
    group: 'performance',
    label: 'Docker Compose',
    active: false,
    priceAdd: 1000
  },
  {
    id: 6,
    group: 'performance',
    label: 'FastAPI backend',
    active: false,
    priceAdd: 20000
  },
  {
    id: 7,
    group: 'visual',
    label: 'GSAP анимации',
    active: false,
    priceAdd: 10000
  },
  {
    id: 8,
    group: 'visual',
    label: '3D визуализация',
    active: false,
    priceAdd: 15000
  },
  {
    id: 9,
    group: 'visual',
    label: 'Лид-формы',
    active: false,
    priceAdd: 1000
  }
])

const currentProject = computed(() =>
  projects.find(p => p.id === selectedProject.value)
)

const currentCMS = computed(() =>
  cmsOptions.find(c => c.id === selectedCMS.value)
)

const marketingOptions = computed(() =>
  options.filter(o => o.group === 'marketing')
)

const performanceOptions = computed(() =>
  options.filter(o => o.group === 'performance')
)

const visualOptions = computed(() =>
  options.filter(o => o.group === 'visual')
)

const activeOptions = computed(() =>
  options.filter(o => o.active)
)

const estimatedTime = computed(() => {

  if (selectedProject.value === 'shop') {
    return '14–30 дней'
  }

  return '5–10 дней'
})

const totalPrice = computed(() => {

  let total = currentProject.value.basePrice

  total += currentCMS.value.priceAdd

  total += activeOptions.value.reduce((sum, option) => {
    return sum + option.priceAdd
  }, 0)

  return total
})

const formattedPrice = computed(() =>
  totalPrice.value.toLocaleString('ru-RU')
)

async function scrollToContact() {

  try {

    await fetch('/api/calculator', {

      method: 'POST',

      headers: {
        'Content-Type': 'application/json',
      },

      body: JSON.stringify({

        type: currentProject.value.title,

        cms: currentCMS.value.label,

        options: activeOptions.value.map(o => o.label),

        price: totalPrice.value,

        time: estimatedTime.value,

      }),

    });

    alert('Конфигурация отправлена');

  } catch (err) {

    console.error(err);

    alert('Ошибка отправки');

  }

}

watch(totalPrice, async () => {

  await nextTick()

  if (!priceRef.value) return

  gsap.fromTo(
    priceRef.value,
    {
      y: 8,
      opacity: 0.5
    },
    {
      y: 0,
      opacity: 1,
      duration: 0.3,
      ease: 'power2.out'
    }
  )
})

onMounted(() => {

  gsap.from('.folder', {
    y: 20,
    opacity: 0,
    stagger: 0.15,
    duration: 0.6,
    ease: 'back.out(1.6)'
  })

  gsap.to('.folder-lights span', {
    opacity: 0.6,
    repeat: -1,
    yoyo: true,
    duration: 1,
    stagger: 0.2
  })
})
</script>
 