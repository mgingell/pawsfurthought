<?php
/**
 * Plugin Name: Local mail trap (Mailpit)
 * Description: Sends every email from this local copy to Mailpit (http://localhost:8025) instead of real inboxes.
 */

add_action( 'phpmailer_init', function ( $phpmailer ) {
	$phpmailer->isSMTP();
	$phpmailer->Host        = 'mailpit';
	$phpmailer->Port        = 1025;
	$phpmailer->SMTPAuth    = false;
	$phpmailer->SMTPAutoTLS = false;
} );

// WordPress defaults to wordpress@localhost, which PHPMailer rejects as invalid
add_filter( 'wp_mail_from', function ( $from ) {
	return str_ends_with( $from, '@localhost' ) ? 'wordpress@pawsfurthought.local' : $from;
} );
