<template>
  <section class="calculator">

    <div class="container">

      <div class="calculator__grid">

        <!-- LEFT -->

        <aside class="calculator__left">

          <span class="calculator__label">
            калькулятор
          </span>

          <h2 class="calculator__title">
            СОБЕРИТЕ<br />
            СВОЮ<br />
            ВКЛАДКУ
          </h2>

          <p class="calculator__description">
            Ответьте на несколько вопросов
            и получите предварительную стоимость
            и сроки запуска проекта.
          </p>

          <!-- VISUAL -->

          <div class="calculator__visual">

            <div class="calculator-folder calculator-folder--back"></div>
            <div class="calculator-folder calculator-folder--middle"></div>

            <div class="calculator-folder calculator-folder--front">

              <div class="calculator-folder__number">
                0{{ tabsCount }}
              </div>

              <div class="calculator-folder__eyes">
                <span></span>
                <span></span>
              </div>

              <div class="calculator-folder__type">
                {{ projectType.title }}
              </div>

            </div>

            <div class="calculator__glow"></div>

          </div>

          <!-- FEATURES -->

          <div class="calculator__features">

            <div class="calculator-feature">

              <div class="calculator-feature__icon">
                ⚡
              </div>

              <div>
                <strong>
                  быстро
                </strong>

                <span>
                  1–2 минуты
                </span>
              </div>

            </div>

            <div class="calculator-feature">

              <div class="calculator-feature__icon">
                ◎
              </div>

              <div>
                <strong>
                  точно
                </strong>

                <span>
                  под ваш проект
                </span>
              </div>

            </div>

            <div class="calculator-feature">

              <div class="calculator-feature__icon">
                🔒
              </div>

              <div>
                <strong>
                  без спама
                </strong>

                <span>
                  данные защищены
                </span>
              </div>

            </div>

          </div>

        </aside>

        <!-- CENTER -->

        <div class="calculator__center">

          <!-- STEP -->

          <div class="calculator-block">

            <div class="calculator-block__top">

              <span class="calculator-block__step">
                01
              </span>

              <h3>
                СКОЛЬКО ВКЛАДОК
                НУЖНО В ПРОЕКТЕ?
              </h3>

            </div>

            <div class="calculator-tabs-count">

              <button
                v-for="item in [1,2,3,4]"
                :key="item"
                :class="[
                  'calculator-tabs-count__button',
                  {
                    active: tabsCount === item
                  }
                ]"
                @click="tabsCount = item"
              >
                0{{ item }}
              </button>

            </div>

          </div>

          <!-- PROJECT TYPES -->

          <div class="calculator-block">

            <div class="calculator-block__top">

              <span class="calculator-block__step">
                02
              </span>

              <h3>
                ВЫБЕРИТЕ
                ТИП ПРОЕКТА
              </h3>

            </div>

            <div class="calculator-types">

              <button
                v-for="item in projectTypes"
                :key="item.id"
                :class="[
                  'calculator-type',
                  {
                    active: projectType.id === item.id
                  }
                ]"
                @click="projectType = item"
              >

                <div class="calculator-type__check">
                  ✓
                </div>

                <h4>
                  {{ item.title }}
                </h4>

                <p>
                  {{ item.description }}
                </p>

                <span>
                  от {{ item.price.toLocaleString('ru-RU') }} ₽
                </span>

              </button>

            </div>

          </div>

          <!-- OPTIONS -->

          <div class="calculator-block">

            <div class="calculator-block__top">

              <span class="calculator-block__step">
                03
              </span>

              <h3>
                ДОПОЛНИТЕЛЬНЫЕ
                ВОЗМОЖНОСТИ
              </h3>

            </div>

            <div class="calculator-options">

              <button
                v-for="option in options"
                :key="option.id"
                class="calculator-option"
                :class="{
                  active: option.enabled
                }"
                @click="option.enabled = !option.enabled"
              >

                <span>
                  {{ option.title }}
                </span>

                <div class="calculator-option__toggle">
                  <div class="calculator-option__circle"></div>
                </div>

              </button>

            </div>

          </div>

        </div>

        <!-- RIGHT -->

        <aside class="calculator__right">

          <div class="calculator-preview">

            <div class="calculator-preview__top">

              <div>

                <span class="calculator-preview__label">
                  LIVE PREVIEW
                </span>

                <h3>
                  01вкладка / concept
                </h3>

              </div>

              <div class="calculator-preview__status">
                deploy-ready
              </div>

            </div>

            <!-- PREVIEW -->

            <div class="calculator-preview__image">

              <img
                src="/images/calculator_preview.webp"
                alt=""
              />

            </div>

            <!-- INFO -->

            <div class="calculator-preview__info">

              <div class="calculator-preview__row">

                <span>
                  тип проекта
                </span>

                <strong>
                  {{ projectType.title }}
                </strong>

              </div>

              <div class="calculator-preview__row">

                <span>
                  вкладок
                </span>

                <strong>
                  0{{ tabsCount }}
                </strong>

              </div>

              <div class="calculator-preview__row">

                <span>
                  stack
                </span>

                <strong>
                  Astro + Vue
                </strong>

              </div>

              <div class="calculator-preview__row">

                <span>
                  доп. возможности
                </span>

                <strong>
                  {{ enabledOptions }}
                </strong>

              </div>

            </div>

            <!-- PRICE -->

            <div class="calculator-price">

              <span class="calculator-price__label">
                предварительная стоимость
              </span>

              <strong class="calculator-price__value">
                {{ finalPrice.toLocaleString('ru-RU') }} ₽
              </strong>

              <span class="calculator-price__meta">
                ориентировочная оценка проекта
              </span>

            </div>

            <!-- DAYS -->

            <div class="calculator-time">

              <span>
                примерный срок
              </span>

              <strong>
                {{ finalDays }} дней
              </strong>

            </div>

            <!-- BUTTON -->

            <button class="calculator__submit">

              ОБСУДИТЬ ПРОЕКТ

              <span>
                →
              </span>

            </button>

          </div>

        </aside>

      </div>

    </div>

  </section>
</template>

<script setup>
import { ref, computed } from 'vue';

const tabsCount = ref(1);

const projectTypes = [
  {
    id: 1,
    title: 'Концепт',
    description: 'структура, визуал и ключевые экраны',
    price: 20000,
  },

  {
    id: 2,
    title: 'Лендинг',
    description: 'продающая страница под продукт',
    price: 45000,
  },

  {
    id: 3,
    title: 'Корп. сайт',
    description: 'многостраничный сайт для компании',
    price: 70000,
  },

  {
    id: 4,
    title: 'Интернет-магазин',
    description: 'каталог, корзина и интеграции',
    price: 120000,
  },
];

const projectType = ref(projectTypes[0]);

const options = ref([
  {
    id: 1,
    title: 'AI-бот / ассистент',
    price: 15000,
    enabled: true,
  },

  {
    id: 2,
    title: 'CRM интеграция',
    price: 10000,
    enabled: true,
  },

  {
    id: 3,
    title: 'SEO оптимизация',
    price: 12000,
    enabled: true,
  },

  {
    id: 4,
    title: 'Анимации и эффекты',
    price: 8000,
    enabled: true,
  },

  {
    id: 5,
    title: 'Каталог / фильтры',
    price: 15000,
    enabled: false,
  },

  {
    id: 6,
    title: 'Мультиязычность',
    price: 10000,
    enabled: false,
  },
]);

const enabledOptions = computed(() => {
  return options.value.filter(item => item.enabled).length;
});

const finalPrice = computed(() => {
  const base =
    projectType.value.price * tabsCount.value;

  const extra =
    options.value
      .filter(item => item.enabled)
      .reduce((sum, item) => sum + item.price, 0);

  return base + extra;
});

const finalDays = computed(() => {
  return 5 + tabsCount.value * 2 + enabledOptions.value;
});
</script>