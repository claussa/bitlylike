$(() => {
	$('.navbutton').click((event) => {
		event.preventDefault();
		$.ajax({
			url: $(event.target).data('url'),
			success: (data) => {
				$('#content').html(data);
			}
		});
	});
	$('#start').click();
	
	$(window).on("beforeunload", () => {
		return "Do you really want to quit ?";
	});
});