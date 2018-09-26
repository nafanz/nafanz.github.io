window.addEvent('domready',function(){
if($('pricelist')){
var table = $('pricelist').getFirst('table');
	var FiltersParams = new Array();//здесь хранить порядковые номара столбцов с фильтрами
	var FiltersData = new Array();//здесь хранить порядковые номара столбцов с фильтрами
	table.getElements('th').each(function(th,index){
		if(th.hasClass('filterable')) {
			FiltersParams[index] = th;
			FiltersData[index] = new Array();
		}
	});
	
	//alert(FiltersData.length);
	
	table.getElements('tr').each(function(tr){
		tr.getElements('td').each(function(td, index){
			if(typeof(FiltersData[index]) != 'undefined'){
				var value = td.get('text');
				if(value == '--') value = 0;
				if(FiltersParams[index].hasClass('table-sortable:numeric')) {value = value.toFloat();}
				FiltersData[index][FiltersData[index].length] = value;
			}
		});
	});
	
	
	FiltersData2 = new Array();
	FiltersData.each(function(item,index){
		var item2 = item.unique();
		item2.each(function(d){
			d = d.toInt();
		});
		FiltersData2[index] = item2;//здесь уникальные значения
		
		/************************* ИЗМ 1 ***************************************/
		//FiltersData2[index].sort(function(a,b){return a.toInt() - b.toInt()}) //Array now becomes [7, 8, 25, 41]
		FiltersData2[index].sort(function(a,b){return a.toFloat() - b.toFloat()}) //Array now becomes [7, 8, 25, 41]
		
	});
	
	//теперь строим выпадалки
	table.getElement('tr.filter_container').getElements('th').each(function(th,index){
		if(typeof(FiltersData2[index]) != 'undefined'){
			var select = th.getElement('select');
			if(select){
				FiltersData2[index].each(function(item){
					/************************* ИЗМ 2 ***************************************/
					if(item != '' || item == 0)
					select.options[select.options.length] = new Option(item, item);
				});
			}
		}
	});
	

}
	/*
	var test = [91,0,5,5.2,3,8,6.4];
	test.sort(function(a,b){return a.toInt() - b.toInt()});
	test.each(function(item){
		alert(item);
	});
	*/
});