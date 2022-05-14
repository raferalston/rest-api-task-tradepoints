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
            <ul>
                <li>phone : 123</li>
                <li>trade_point : 1</li>
                <li>latitude : 1.0</li>
                <li>longitude : 1.0</li>
            </ul>
        </td>
        <td>
            Add new visit to a trade point
        </td>
    </tr>
<table>

