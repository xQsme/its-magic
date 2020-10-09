<script lang="ts">
    import { auth } from '../utils/stores';
</script>

<div class="login-container">
    <h1>Login</h1>
    <a href="/"><button on:click={() => auth.set({email: 'altesbesta@mail.com', username: 'Altes Besta', role: 'ADMIN', token: 'JWT'})}>Admin</button></a>
    <a href="/"><button on:click={() => auth.set({email: 'Yvtq8K3n@mail.com', username: 'Yvtq8K3n', role: 'USER', token: 'JWT'})}>User</button></a>
</div>

<style lang="scss">
    .login-container{
        text-align: center;
        width: 100%;
    }
</style>