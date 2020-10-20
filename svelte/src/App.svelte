<script lang="ts">
	import Game from './components/Game.svelte';
	import Login from './components/Login.svelte';
	import Register from './components/Register.svelte';
	import Enemies from './components/Enemies.svelte';
	import Spells from './components/Spells.svelte';
	import Colors from './components/Colors.svelte';
	import Player from './components/Player.svelte';
	import Users from './components/Users.svelte';
	import router from 'page';
	import { auth } from './utils/stores';
	import { beforeUpdate } from 'svelte';
	import { get } from 'svelte/store';
	import { setupReqRes } from './utils/req';
	setupReqRes();

	let role = get(auth) ? get(auth).role : null;
	export let page;
	export let params;

	router('/login', () => page = Login);
	router('/register', () => page = Register);

	router('/', () => {
		authMiddleware();
		page = Game
	});

	router('/enemies', () => {
		adminMiddleware();
		page = Enemies
	});
	router('/spells', () => {
		adminMiddleware();
		page = Spells
	});
	router('/colors', () => {
		adminMiddleware();
		page = Colors
	});

	router('/*', () => {
		router.redirect('/');
	})
	
	router.start();

	function authMiddleware () {
		if(get(auth) === null) {
			router.redirect('/login');
		}
	}
	
	function adminMiddleware() {
		if(get(auth) === null || !get(auth).role.includes("ADMIN")) {
			router.redirect('/');
		}
	}

	beforeUpdate(() => {
		role = get(auth) ? get(auth).role : null;
	});

</script>


<svelte:head>
	<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
	<link rel="stylesheet" href="assets/styles/app.css">

</svelte:head>
<main>
	<nav class="nav-bar">
		<a href="/" class="logo">
			<img class="logo-icon" src="assets/images/wand.png" alt="logo" />
			<span class="logo-text">It's Magic</span>
		</a>
		<div class="pages">
			{#if role!= null && role.includes("ADMIN")}
				<a href="/player" class:active={page === Player}>Player</a>
				<a href="/enemies" class:active={page === Enemies}>Enemies</a>
				<a href="/spells" class:active={page === Spells}>Spells</a>
				<a href="/colors" class:active={page === Colors}>Colors</a>
				<a href="/users" class:active={page === Users}>Users</a>
			{/if}
			{#if role === null}
				<a href="/login" class:active={page === Login}>Login</a>
				<a href="/register" class:active={page === Register}>Register</a>
			{/if}
			{#if role !== null}
				<a href="/" on:click={evt => auth.set(null)}>Logout</a>
			{/if}
		</div>
	</nav>
	<div class="main-container">
		<svelte:component this={page} params={params} />
	</div>
</main>

<style type="text/scss">
	main{
		display: flex;
		flex-direction: column;
		width: 100%;
		height: 100%;

		.nav-bar{
			height: 55px;
			width: 100%;
			display: flex;
			align-items: center;
			background-color: #303030;
			flex: 0 0 auto;

			.logo{
				display: flex;
				align-items: center;
				margin-left: 20px;

				.logo-icon{
					height: 30px;
				}

				.logo-text{
					font-size: 20px;
				}
			}

			.pages{
				margin-left: auto;
				margin-right: 20px;
			}

			a{
				color: white;
				margin: 0 10px;
				text-decoration: none;
			}

			a:last-of-type{
				margin-right: 0;
			}

			.active{
				color: orangered;
			}

			a:not(.logo):hover{
				color: orangered;
			}
		}

		.main-container{
			display: flex;
			width: 100%;
        	height: calc(100% - 55px);
		}
	}
</style>