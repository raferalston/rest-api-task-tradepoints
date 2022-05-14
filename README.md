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
            /api/tradepoints?phone=123
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
    <tr>
        <td>
            /api/admin/workers
        </td>
        <td>
            GET, POST, HEAD, OPTIONS
        </td>
        <td>
            <ul>
                <li>name : foo</li>
                <li>phone : 123</li>
            </ul>
        </td>
        <td>
            Create or Retrieve worker
        </td>
    </tr>
    <tr>
        <td>
            /api/admin/workers/{int:pk}
        </td>
        <td>
            GET, PUT, PATCH, DELETE, HEAD, OPTIONS
        </td>
        <td>
            <ul>
                <li>name : foo</li>
                <li>phone : 123</li>
            </ul>
        </td>
        <td>
            CRUD for worker
        </td>
    </tr>
    <tr>
        <td>
            /api/admin/workers/search/{name}
        </td>
        <td>
            GET, HEAD, OPTIONS
        </td>
        <td>
            <ul>
                <li>name: foo</li>
            </ul>
        </td>
        <td>
            Retrieve worker
        </td>
    </tr>
    <tr>
        <td>
            /api/admin/tradepoints
        </td>
        <td>
            GET, POST, HEAD, OPTIONS
        </td>
        <td>
            <ul>
                <li>name : foo</li>
                <li>worker : 1 (id)</li>
            </ul>
        </td>
        <td>
            Create or Retrieve trade point
        </td>
    </tr>
    <tr>
        <td>
            /api/admin/tradepoints/{int:pk}
        </td>
        <td>
            GET, PUT, PATCH, DELETE, HEAD, OPTIONS
        </td>
        <td>
            <ul>
                <li>name : foo</li>
                <li>worker : 1 (id)</li>
            </ul>
        </td>
        <td>
            CRUD for trade point
        </td>
    </tr>
    <tr>
        <td>
            /api/admin/tradepoints/search/{name}
        </td>
        <td>
            GET, HEAD, OPTIONS
        </td>
        <td>
            <ul>
                <li>name : foo</li>
            </ul>
        </td>
        <td>
            Retrieve trade point
        </td>
    </tr>
    <tr>
        <td>
            /api/admin/visits
        </td>
        <td>
            GET, HEAD, OPTIONS
        </td>
        <td>
        </td>
        <td>
            Retrieve visits
        </td>
    </tr>
    <tr>
        <td>
            /api/admin/visits/{int:pk}
        </td>
        <td>
            GET, HEAD, OPTIONS
        </td>
        <td>
            <ul>
                <li>int:pk : 1</li>
            </ul>
        </td>
        <td>
            Retrieve visits by id
        </td>
    </tr>
    <tr>
        <td>
            /api/admin/visits/tradepoint-search/{tradepoint}
        </td>
        <td>
            GET, HEAD, OPTIONS
        </td>
        <td>
            <li>tradepoint : foo</li>
        </td>
        <td>
            Retrieve visits by name
        </td>
    </tr>
    <tr>
        <td>
            /api/admin/visits/worker-search/{worker}
        </td>
        <td>
            GET, HEAD, OPTIONS
        </td>
        <td>
            <li>worker : foo</li>
        </td>
        <td>
            Retrieve visits by worker name
        </td>
    </tr>
    <tr>
        <td>
            /api/admin/visits/search/?worker=foo
        </td>
        <td>
            GET, HEAD, OPTIONS
        </td>
        <td>
            <li>?worker=[name] : foo</li>
            <li>?tradepoint=[name] : foo</li>
        </td>
        <td>
            Retrieve visits by worker name or tradepoint name with url params
        </td>
    </tr>
<table>

