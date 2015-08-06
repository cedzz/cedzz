var get_random_value = function(arr) {
	// if(typeof(arr) === 'array') {
		return arr[Math.floor(Math.random() * arr.length)];
	// }
	return null;
};

var tool = function() {
	var arr = ['nunchaks', 'katana', 'shuriken', 'kunai'];
	return get_random_value(arr);
};

var kunoichi = function() {
	var arr = ['sakura' , 'ino', 'tenten'];
	return get_random_value(arr);
};


var ninja = function() {
	var kuno = kunoichi();

	var __ninja = function() {
		var my_tool = tool();
	
		console.log('This is a constructor with ' +
		 'object kuno having value ' + kuno + ' having tool:' + my_tool);
	}

	// I am calling constructor two times , just for fun :p
	__ninja();
	__ninja();
};

// now i am calling the ninja two times. 

ninja(); 
ninja();