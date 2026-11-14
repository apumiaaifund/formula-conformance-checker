# Formula Conformance Checker (FCC) — Public Demo

## За 30 секунд

**Что это:** FCC: 57 формул, 76 векторов, 25 инвариантов. SARIF 2.1.0. Manifest conformance.json. Model risk management.

**Кому:** Банки, страховые — SR 11-7 / SOX / model risk. Интеграция 300–500K ₽.

**Что доказано:** 12 passed. QuantLib 1.44: 19/19 совпали (6 из 25 не дописаны — честно).

**Чего не доказано (честно):** CI на GitHub не запускался. QuantLib покрытие 19/25, не полное.

---



**Offline CLI-валидатор финансовых формул.** Проверяет, что реализации
финансовых формул в вашем коде совпадают с эталонами из литературы —
через тест-векторы, математические инварианты и unit-валидацию входов.

**Demo materials only. Full source code — available on purchase.**

Zero runtime-зависимостей (stdlib Python >= 3.10). Работает офлайн.
Встраивается в CI через JSON / Markdown / SARIF 2.1.0 отчёты.

## Зачем

Model risk management (SR 11-7 в US, TRIM в EU, SOX-контроль в аудите)
требует, чтобы расчёты были воспроизводимы и подтверждены независимо.
FCC — это способ доказать, что формула в проде считает то, что должна.

## Что проверяется

- **57 формул**: TVM, Altman (3 варианта), Black-Scholes (+5 греков), Merton,
  Sharpe/Sortino/Calmar/Treynor/MDD, CAPM/beta/alpha, WACC, VaR
  (parametric/historical/CVaR), облигации (price + duration + convexity),
  портфельная математика, multiples, DDM, коэффициенты отчётности.
- **76 тест-векторов** с источниками (Hull, Brealey-Myers, Fabozzi,
  Damodaran, Altman 1983/1995, Merton 1974, Rockafellar).
- **25 математических инвариантов**: NPV(IRR)=0, put-call parity,
  beta(x,x)=1, MDD в [-1,0], WACC(E,0)=Re, rho(x,x)=1 и др.
- **Unit-валидация входов**: типы, диапазоны, NaN/Inf, integer-поля.

## Два режима подключения

1. Декоратор в коде:

    from formula_conformance import validate

    @validate("altman_z_public")
    def altman_z(...):
        ...

2. Manifest conformance.json — без правки продакшн-кода:

    {
      "formulas": {
        "altman_z_public": "myapp.finance:altman_z",
        "capm_expected_return": "myapp.finance:capm"
      }
    }

## CLI

    fcc check --target path/to/your/file.py
    fcc check --manifest conformance.json
    fcc check --target file.py --sarif      # SARIF 2.1.0 для GitHub Code Scanning
    fcc verify                              # сверить эталоны с векторами
    fcc formulas                            # список всех формул с источниками
    fcc explain black_scholes_call          # векторы + инварианты одной формулы

Exit codes: 0 — успех, 1 — найдены critical, 2 — internal error.

## Что подтверждено прогоном

| Метрика | Значение |
|---|---|
| Формул | 57 |
| Тест-векторов | 76, 0 расхождений |
| Инвариантов | 25 |
| Unit-тестов | 12, все ok |
| CLI-команд | 4 |
| QuantLib 1.44 (внешняя сверка) | 19/19 совпали |
| SARIF | 2.1.0 |

## Что честно НЕ закрыто

- QuantLib-сверка: 19 кейсов из 25 заявленных. 6 «по аналогии» не дописаны.
- CI на GitHub не запускался (yaml прогонялся локально).

## Цена

| Уровень | Цена | Что |
|---|---|---|
| Pilot / интеграция | 300–500K ₽ | Внедрение под ваш домен + golden dataset |
| Enterprise | по запросу | Приватный репо + ZIP + поддержка |

Контакт: [apumiaaifund@gmail.com](mailto:apumiaaifund@gmail.com)

## Лицензия

Proprietary. См. LICENSE. Исходный код — по запросу.

**No synthetic data in production.** Все цифры в этом README подтверждены
прогонами; ничего не придумано.
