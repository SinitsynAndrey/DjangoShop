window.onload = function() {
    let _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;
    let quantity_arr = [];
    let cost_arr = [];

    const TOTAL_FORMS = $('input[name="orderitems-TOTAL_FORMS"]').val();


    let order_total_quantity = parseInt($('.order_total_quantity').text()) || 0;
    let order_total_cost = parseFloat($('.order_total_cost').text().replace(',','.')) || 0;

    for(let i=0; i < TOTAL_FORMS; i++) {
    _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
    _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',','.'));
    quantity_arr.push(_quantity)
    if (_price){
        cost_arr.push(_price)
    } else {
        cost_arr.push(0)
        }
    }

    if (!order_total_quantity) {
        for (let i=0; i < TOTAL_FORMS; i++) {
            order_total_quantity += quantity_arr[i];
            order_total_cost += quantity_arr[i] * cost_arr[i];
        }
        $('.order_total_quantity').html(order_total_quantity.toString());
        $('.order_total_cost').html(Number(order_total_cost.toFixed(2)).toString());
    }

$('.order_form').on('click', 'input[type="number"]', function() {
    let target = event.target;
    orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
    if (cost_arr[orderitem_num]){

        orderitem_quantity = parseInt(target.value);
        delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
        quantity_arr[orderitem_num] = orderitem_quantity;
        orderSummaryUpdate(cost_arr[orderitem_num], delta_quantity);
    }
});

$('.order_form').on('click', 'input[type="checkbox"]', function() {
    let target = event.target;
    orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-DELETE', ''));

    if (target.checked) {
        delta_quantity = -quantity_arr[orderitem_num];
    } else {
        delta_quantity = quantity_arr[orderitem_num];
    }
    orderSummaryUpdate(cost_arr[orderitem_num], delta_quantity)
});

function orderSummaryUpdate(orderitem_price, delta_quantity){
    delta_cost = orderitem_price * delta_quantity

    order_total_cost = Number((order_total_cost + delta_cost).toFixed(2));
    order_total_quantity += delta_quantity;

    $('.order_total_cost').html(order_total_cost.toString());
    $('.order_total_quantity').html(order_total_quantity.toString());
}

$('.formset_row').formset({
    addText: 'добавить продукт',
    deleteText: 'удалить',
    prefix: 'orderitems',
    removed: deleteOrderItem
});

function deleteOrderItem(row) {
   let target_name= row[0].querySelector('input[type="number"]').name;
   orderitem_num = parseInt(target_name.replace('orderitems-', '').replace('-quantity', ''));
   delta_quantity = -quantity_arr[orderitem_num];
   orderSummaryUpdate(cost_arr[orderitem_num], delta_quantity);
}

$('.order_form select').change(function () {
   let target = event.target;
   console.log(target);
});

}
