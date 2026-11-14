"""Сломанная реализация — валидатор должен поймать."""
from formula_conformance import validate


@validate("altman_z_public")
def altman_z(working_capital, retained_earnings, ebit, mve, sales,
             total_assets, total_liabilities):
    x1 = working_capital / total_assets
    x2 = retained_earnings / total_assets
    x3 = ebit / total_assets
    x4 = mve / total_liabilities
    x5 = sales / total_assets
    return 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1.0 * x5   # пропущен 1.2*x1


@validate("capm_expected_return")
def capm(Rf, beta, Rm):
    return Rf - beta * (Rm - Rf)   # знак
