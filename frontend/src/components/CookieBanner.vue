<template>

  <!-- COOKIE -->

  <transition name="cookie-fade">

    <div
      v-if="showCookie"
      class="cookie-banner"
    >

      <div class="cookie-banner__window">

        <div class="cookie-banner__glow"></div>

        <div class="cookie-banner__content">

          <div class="cookie-banner__label">
            cookies & privacy
          </div>

          <h3 class="cookie-banner__title">
            ИСПОЛЬЗУЕМ COOKIES
            <br />
            И ДАННЫЕ ФОРМ
          </h3>

          <p class="cookie-banner__text">

            Мы используем cookies, Яндекс.Метрику
            и данные форм связи для аналитики,
            обработки заявок и улучшения работы сайта.

          </p>

          <div class="cookie-banner__actions">

            <button
              class="cookie-banner__accept"
              @click="acceptCookies"
            >
              принять
            </button>

            <button
              class="cookie-banner__policy"
              @click="openPolicy"
            >
              политика
            </button>

          </div>

        </div>

      </div>

    </div>

  </transition>

  <!-- POLICY -->

  <transition name="cookie-fade">

    <div
      v-if="showPolicy"
      class="policy-modal"
      @click="closePolicy"
    >

      <div
        class="policy-modal__window"
        @click.stop
      >

        <button
          class="policy-modal__close"
          @click="closePolicy"
        >
          ×
        </button>

        <div class="policy-modal__scroll">

          <div class="policy-modal__label">
            политика конфиденциальности
          </div>

          <h2 class="policy-modal__title">
            ПОЛИТИКА ОБРАБОТКИ
            ПЕРСОНАЛЬНЫХ ДАННЫХ
          </h2>

          <div class="policy-modal__content">

            <p>
              Настоящая политика обработки персональных данных
              определяет порядок обработки и защиты информации,
              предоставляемой пользователями сайта 01вкладка.рф.
            </p>

            <h3>
              1. Общие положения
            </h3>

            <p>
              Использование сайта означает согласие пользователя
              с настоящей политикой обработки персональных данных
              и условиями обработки его информации.
            </p>

            <h3>
              2. Какие данные собираются
            </h3>

            <ul>

              <li>
                имя пользователя;
              </li>

              <li>
                номер телефона;
              </li>

              <li>
                адрес электронной почты;
              </li>

              <li>
                сообщения, отправленные через формы сайта;
              </li>

              <li>
                техническая информация браузера и устройства;
              </li>

              <li>
                cookies и данные аналитики.
              </li>

            </ul>

            <h3>
              3. Цели обработки данных
            </h3>

            <ul>

              <li>
                обработка заявок;
              </li>

              <li>
                обратная связь с пользователем;
              </li>

              <li>
                подготовка коммерческих предложений;
              </li>

              <li>
                аналитика и улучшение работы сайта;
              </li>

              <li>
                обеспечение безопасности сайта.
              </li>

            </ul>

            <h3>
              4. Cookies и аналитика
            </h3>

            <p>
              Сайт использует cookies,
              а также сервис Яндекс.Метрика
              для анализа поведения пользователей,
              улучшения интерфейсов
              и повышения качества работы сайта.
            </p>

            <h3>
              5. Хранение и защита данных
            </h3>

            <p>
              Персональные данные хранятся
              на защищённых серверах
              и не передаются третьим лицам,
              за исключением случаев,
              предусмотренных законодательством РФ.
            </p>

            <h3>
              6. Права пользователя
            </h3>

            <p>
              Пользователь вправе запросить
              изменение или удаление
              своих персональных данных,
              направив запрос через контактные данные сайта.
            </p>

            <h3>
              7. Контакты
            </h3>

            <p>
              Email:
              privet@01вкладка.рф
            </p>

            <p>
              Телефон:
              +7 (977) 865-68-28
            </p>

          </div>

        </div>

      </div>

    </div>

  </transition>

</template>

<script setup>
import {
  ref,
  onMounted,
  onUnmounted
} from 'vue';

/* ======================================
   STATE
====================================== */

const showCookie = ref(false);

const showPolicy = ref(false);

/* ======================================
   MOUNT
====================================== */

onMounted(() => {

  const accepted =
    localStorage.getItem('cookie-accepted');

  if (!accepted) {

    setTimeout(() => {

      showCookie.value = true;

    }, 1200);

  }

  window.addEventListener(
    'open-policy',
    handleOpenPolicy
  );

});

onUnmounted(() => {

  window.removeEventListener(
    'open-policy',
    handleOpenPolicy
  );

});

/* ======================================
   ACCEPT
====================================== */

function acceptCookies() {

  localStorage.setItem(
    'cookie-accepted',
    'true'
  );

  showCookie.value = false;

}

/* ======================================
   POLICY
====================================== */

function openPolicy() {

  showPolicy.value = true;

}

function closePolicy() {

  showPolicy.value = false;

}

function handleOpenPolicy() {

  showPolicy.value = true;

}
</script>

<style scoped lang="scss">
.cookie-banner {
  position: fixed;

  left: 24px;
  right: 24px;
  bottom: 24px;

  z-index: 9999;

  display: flex;
  justify-content: center;

  pointer-events: none;

  &__window {
    position: relative;

    width: 100%;
    max-width: 560px;

    overflow: hidden;

    border:
      1px solid rgba(255,255,255,.06);

    border-radius: 28px;

    background:
      rgba(7,10,14,.92);

    backdrop-filter: blur(18px);

    box-shadow:
      0 30px 80px rgba(0,0,0,.45);

    pointer-events: auto;
  }

  &__glow {
    position: absolute;

    top: -120px;
    right: -120px;

    width: 260px;
    height: 260px;

    border-radius: 50%;

    background:
      radial-gradient(
        rgba(217,255,0,.16),
        transparent 70%
      );
  }

  &__content {
    position: relative;

    z-index: 2;

    padding:
      28px
      28px
      26px;
  }

  &__label {
    margin-bottom: 18px;

    color: #d9ff00;

    font-size: 10px;
    font-weight: 700;

    letter-spacing: .18em;

    text-transform: uppercase;
  }

  &__title {
    margin-bottom: 16px;

    color: #fff;

    font-family: var(--font-display);

    font-size: var(--title-medium);

    line-height: .92;

    letter-spacing: -.05em;

    text-transform: uppercase;
  }

  &__text {
    margin-bottom: 26px;

    color:
      rgba(255,255,255,.58);

    font-size: 14px;

    line-height: 1.7;
  }

  &__actions {
    display: flex;
    gap: 12px;

    @media (max-width: 640px) {
      flex-direction: column;
    }
  }

  &__accept,
  &__policy {
    height: 54px;

    padding:
      0
      22px;

    border-radius: 16px;

    font-size: 14px;
    font-weight: 700;

    cursor: pointer;

    transition:
      .25s ease;
  }

  &__accept {
    border: none;

    background: #d9ff00;

    color: #000;

    &:hover {
      transform: translateY(-2px);
    }
  }

  &__policy {
    border:
      1px solid rgba(255,255,255,.06);

    background:
      rgba(255,255,255,.03);

    color: #fff;

    &:hover {
      border-color:
        rgba(217,255,0,.16);

      color: #d9ff00;
    }
  }
}

/* ======================================
   POLICY
====================================== */

.policy-modal {
  position: fixed;
  inset: 0;

  z-index: 10000;

  display: flex;
  align-items: center;
  justify-content: center;

  padding: 20px;

  background:
    rgba(5,7,11,.82);

  backdrop-filter: blur(14px);

  &__window {
    position: relative;

    width: 100%;
    max-width: 860px;

    max-height: 86vh;

    overflow: hidden;

    border:
      1px solid rgba(255,255,255,.06);

    border-radius: 30px;

    background:
      linear-gradient(
        180deg,
        rgba(9,12,18,.98) 0%,
        rgba(5,7,11,.98) 100%
      );
  }

  &__scroll {
    max-height: 86vh;

    overflow-y: auto;

    padding:
      46px
      42px;

    @media (max-width: 768px) {
      padding:
        34px
        22px;
    }
  }

  &__close {
    position: absolute;

    top: 16px;
    right: 16px;

    width: 42px;
    height: 42px;

    border: none;

    border-radius: 12px;

    background:
      rgba(255,255,255,.04);

    color: #fff;

    font-size: 24px;

    cursor: pointer;
  }

  &__label {
    margin-bottom: 18px;

    color: #d9ff00;

    font-size: 10px;
    font-weight: 700;

    letter-spacing: .18em;

    text-transform: uppercase;
  }

  &__title {
    margin-bottom: 34px;

    color: #fff;

    font-family: var(--font-display);

    font-size: var(--title-medium);

    line-height: .92;

    letter-spacing: -.05em;

    text-transform: uppercase;
  }

  &__content {

    color:
      rgba(255,255,255,.72);

    font-size: 15px;

    line-height: 1.9;

    h3 {
      margin:
        34px
        0
        16px;

      color: #fff;

      font-size: 18px;
    }

    p {
      margin-bottom: 16px;
    }

    ul {
      display: flex;
      flex-direction: column;

      gap: 12px;

      padding-left: 20px;

      margin-bottom: 20px;
    }
  }
}

/* ======================================
   TRANSITIONS
====================================== */

.cookie-fade-enter-active,
.cookie-fade-leave-active {
  transition:
    opacity .25s ease,
    transform .25s ease;
}

.cookie-fade-enter-from,
.cookie-fade-leave-to {
  opacity: 0;

  transform:
    translateY(10px);
}
</style>