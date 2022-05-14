# REST-API for delivery products to shops

<table>
    <caption>Basic API instructions</caption>
    <tr>
        <td>
            Reference
        </td>
        <td>
            Method
        </td>
        <td>
            Params
        </td>
        <td>
            Purpose
        </td>
    </tr>
    <tr>
        <td>
            /api
        </td>
        <td>
            GET
        </td>
        <td>
            None
        </td>
        <td>
            Entry point for basic api
        </td>
    </tr>
        <tr>
        <td>
            /api/tradepoints
        </td>
        <td>
            GET
        </td>
        <td>
            ?phone=[phone-number]
        </td>
        <td>
            List of all tradepoints with basic permission. Need to send phone param
        </td>
    </tr>
        </tr>
        <tr>
        <td>
            /api/visit-trade-point
        </td>
        <td>
            POST
        </td>
        <td>
            - phone : 123
            - trade_point : 1
            - latitude : 1.0
            - longitude : 1.0
        </td>
        <td>
            List of all tradepoints with basic permission. Need to send phone param
        </td>
    </tr>
<table>

