let scope = {shortcut: [], token: "", alert: true}

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
});