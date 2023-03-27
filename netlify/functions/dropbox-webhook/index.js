// Based on: https://github.com/jimniels/netlibox/blob/master/src/_netlify-functions/dropbox-webhook.js
// via: https://www.netlify.com/blog/2018/10/15/combining-netlify-with-dropbox-for-a-one-click-publishing-process/

exports.handler = function (event, context, callback) {
	const { headers, queryStringParameters } = event;

	// Dropbox first hits this endpoint to verify the app will respond to it.
	// It will include a query string parameter called `challenge` which we'll
	// echo back to Dropbox.
	// https://www.dropbox.com/developers/reference/webhooks#tutorial
	if (queryStringParameters.challenge) {
		const msg =
			"Success: Verification request received and responded to appropriately.";
		callback(null, {
			statusCode: 200,
			body: queryStringParameters.challenge,
			headers: {
				"Content-Type": "text/plain",
				"X-Content-Type-Options": "nosniff",
			},
		});
		console.log(msg);
		return;
	}

	if (!headers["x-dropbox-signature"]) {
		const msg =
			"Failed: The request was not what was expected so nothing happened.";
		callback(null, {
			statusCode: 500,
			body: msg,
		});
		console.log(msg, JSON.stringify(event));
		return;
	}

	if (!process.env.NETLIFY_BUILD_HOOK_URL) {
		const msg =
			"Failed: The `NETLIFY_BUILD_HOOK_URL` environment variable is missing.";
		callback(null, {
			statusCode: 500,
			body: msg,
		});
		console.log(msg);
		return;
	}

	fetch(process.env.NETLIFY_BUILD_HOOK_URL, {
		method: "POST",
		body: "",
	})
		.then((res) => {
			const msg =
				"Success: Webhook received from Dropbox and forwarded to Netlify!";
			callback(null, {
				statusCode: 200,
				body: msg,
			});
			console.log(msg);
		})
		.catch((err) => {
			const msg =
				"Failed: Webhook received from Dropbox, but there was an error when forwarding to Netlify.";
			callback(null, {
				statusCode: 500,
				body: err,
			});
			console.log(msg, err);
		});
};
