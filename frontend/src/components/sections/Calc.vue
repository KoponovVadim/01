<script setup>
import { computed, ref } from 'vue'

const popupOpened = ref(false)

const categories = [
  {
    id: 'concept',

    label: 'Концепт',

    title: 'Концепт',

    price: 'от 20 000 ₽',

    description:
      'Быстрый запуск визуальной идеи или digital-концепции с акцентом на стиль и подачу.',

    duration: '3–5 дней',

    includes: [
      'уникальный стиль',
      'адаптивная версия',
      'анимация',
      '1–2 страницы',
      'UI-концепция',
    ],

    styles: [
      {
        title: 'Крафт',
        accent: '#d7ff2f',
        main: '/images/concept_food_main.webp',
      },

      {
        title: 'Неон',
        accent: '#2f6bff',
        main: '/images/concept_him_main.webp',
      },

      {
        title: 'Техно',
        accent: '#d7ff2f',
        main: '/images/concept_service_main.webp',
      },
    ],
  },

  {
    id: 'landing',

    label: 'Лендинг',

    title: 'Лендинг',

    price: 'от 35 000 ₽',

    description:
      'Одностраничный сайт для услуг, продукта или компании с сильной подачей.',

    duration: '5–10 дней',

    includes: [
      'уникальный дизайн',
      'адаптив',
      'анимация',
      'формы заявок',
      'SEO-структура',
    ],

    styles: [
      {
        title: 'Эстетика',
        accent: '#c8a8a1',
        main: '/images/landing_cosmet_main.webp',
      },

      {
        title: 'Архитектура',
        accent: '#ffbf36',
        main: '/images/landing_remont_main.webp',
      },

      {
        title: 'Минимал',
        accent: '#7367ff',
        main: '/images/landing_repet_main.webp',
      },
    ],
  },

  {
    id: 'shop',

    label: 'Магазин',

    title: 'Магазин',

    price: 'от 85 000 ₽',

    description:
      'Интернет-магазин с каталогом, корзиной и системой управления товарами.',

    duration: '10–20 дней',

    includes: [
      'каталог товаров',
      'корзина',
      'CMS-управление',
      'адаптив',
      'SEO-структура',
    ],

    styles: [
      {
        title: 'Тюнинг',
        accent: '#ff3131',
        main: '/images/shop_car_main.webp',
      },

      {
        title: 'Питомцы',
        accent: '#8aa84f',
        main: '/images/shop_pet_main.webp',
      },

      {
        title: 'Брутал',
        accent: '#d7ff2f',
        main: '/images/shop_protein_main.webp',
      },
    ],
  },

  {
    id: 'business',

    label: 'Бизнес',

    title: 'Бизнес',

    price: 'от 100 000 ₽',

    description:
      'Digital-системы и сайты для компаний со сложной структурой и сервисами.',

    duration: '15–30 дней',

    includes: [
      'многостраничность',
      'интерфейсы',
      'CMS',
      'адаптив',
      'SEO',
      'анимация',
    ],

    styles: [
      {
        title: 'Корпорат',
        accent: '#6f58ff',
        main: '/images/business_educ_main.webp',
      },

      {
        title: 'SaaS',
        accent: '#4f6fff',
        main: '/images/business_it_main.webp',
      },

      {
        title: 'Премиум',
        accent: '#c89b62',
        main: '/images/business_law_main.webp',
      },
    ],
  },
]

const activeCategory = ref('business')
const activeStyle = ref(0)

const currentCategory = computed(() =>
  categories.find((item) => item.id === activeCategory.value)
)

const currentStyle = computed(
  () => currentCategory.value.styles[activeStyle.value]
)

const nextStyle = () => {
  activeStyle.value =
    (activeStyle.value + 1) %
    currentCategory.value.styles.length
}

const prevStyle = () => {
  activeStyle.value =
    (activeStyle.value - 1 + currentCategory.value.styles.length) %
    currentCategory.value.styles.length
}

const switchCategory = (id) => {
  activeCategory.value = id
  activeStyle.value = 0
}
</script>

<template>
<a name="calculator"></a>
  <section
    class="showcase"
    :style="{
      '--accent': currentStyle.accent,
    }"
  >
    <div class="container">
      <div class="showcase__grid">
        <aside class="showcase__left">
          <div class="showcase__label">
            <span></span>
            DIGITAL НАПРАВЛЕНИЕ
          </div>

          <h2 class="showcase__title">
            {{ currentCategory.title }}
          </h2>

          <div class="showcase__price">
            {{ currentCategory.price }}
          </div>

          <p class="showcase__description">
            {{ currentCategory.description }}
          </p>

          <div class="showcase__includes">
            <div
              v-for="item in currentCategory.includes"
              :key="item"
              class="showcase__include"
            >
              <span></span>
              {{ item }}
            </div>
          </div>

          <div class="showcase__footer">
            <div class="showcase__duration">
              Срок разработки:
              <strong>{{ currentCategory.duration }}</strong>
            </div>
          <button
          class="showcase__button"
          data-popup
          type="button"
          aria-label="Обсудить проект"
          >
          обсудить проект
        </button>
          </div>
        </aside>

        <div class="showcase__right">
          <div class="showcase__tabs">
            <button
              v-for="category in categories"
              :key="category.id"
              class="showcase__tab"
              :class="{ active: activeCategory === category.id }"
              @click="switchCategory(category.id)"
            >
              {{ category.label }}
            </button>
          </div>

          <div
            class="showcase__preview"
            @click="popupOpened = true"
          >
            <img
              :src="currentStyle.main"
              :alt="currentStyle.title"
            />

            <div class="showcase__preview-overlay">
              <button
                class="showcase__arrow"
                @click.stop="prevStyle"
              >
                ←
              </button>

              <div class="showcase__style-tabs">
                <button
                  v-for="(style, index) in currentCategory.styles"
                  :key="style.title"
                  class="showcase__style-tab"
                  :class="{ active: activeStyle === index }"
                  @click.stop="activeStyle = index"
                >
                  {{ style.title }}
                </button>
              </div>

              <button
                class="showcase__arrow"
                @click.stop="nextStyle"
              >
                →
              </button>
            </div>
          </div>

          <div class="showcase__mobile-tabs">
            <button
              v-for="(style, index) in currentCategory.styles"
              :key="style.title"
              class="showcase__style-tab"
              :class="{ active: activeStyle === index }"
              @click="activeStyle = index"
            >
              {{ style.title }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <Transition name="popup">
      <div
        v-if="popupOpened"
        class="showcase-popup"
        @click="popupOpened = false"
      >
        <button
          class="showcase-popup__close"
          @click="popupOpened = false"
        >
          ×
        </button>

        <img
          :src="currentStyle.main"
          :alt="currentStyle.title"
          @click.stop
        />
      </div>
    </Transition>
  </section>
</template>