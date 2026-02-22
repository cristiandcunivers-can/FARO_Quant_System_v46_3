import json

async def render_ui(assets_input, risk_level, data=None):

    metrics_html = ""

    if data:
        metrics_html = f"""
        <div class="mt-6 p-4 bg-gray-100 rounded-xl shadow">
            <h2 class="text-xl font-semibold mb-2">Resultados</h2>
            <p><strong>Retorno anual esperado:</strong> {round(data['expected_return_annual']*100,2)}%</p>
            <p><strong>Volatilidad anual:</strong> {round(data['volatility_annual']*100,2)}%</p>
            <p><strong>Sharpe Ratio:</strong> {round(data['sharpe_ratio'],2)}</p>
            <p><strong>CVaR 95%:</strong> {round(data['cvar_95']*100,2)}%</p>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>FARO Quant System</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-50 flex items-center justify-center min-h-screen">
        <div class="bg-white p-8 rounded-2xl shadow-lg w-full max-w-lg">
            <h1 class="text-2xl font-bold mb-6 text-center">FARO Quant System</h1>

            <form method="post">
                <label class="block mb-2 font-medium">Tickers (ej: AAPL,MSFT,GOOGL)</label>
                <input name="assets" class="w-full p-2 border rounded mb-4" value="{','.join(assets_input) if assets_input else ''}" required>

                <label class="block mb-2 font-medium">Perfil de Riesgo</label>
                <select name="risk_level" class="w-full p-2 border rounded mb-4">
                    <option {"selected" if risk_level=="Conservador" else ""}>Conservador</option>
                    <option {"selected" if risk_level=="Neutro" else ""}>Neutro</option>
                    <option {"selected" if risk_level=="Agresivo" else ""}>Agresivo</option>
                </select>

                <button class="w-full bg-black text-white p-2 rounded-xl">
                    Ejecutar FARO
                </button>
            </form>

            {metrics_html}
        </div>
    </body>
    </html>
    """
