<script lang="ts">
    import { DialogOverlay, DialogContent } from 'svelte-accessible-dialog';
    import axios from 'axios';
    import { url } from '../utils/server';
    import type { PlayerModel } from '../utils/models';

    let curr:PlayerModel = null;
</script>

<DialogOverlay isOpen={curr !== null} onDismiss={() => curr = null}>
    <DialogContent class="dialog" aria-label="Announcement">
        <form class="dialog-container" on:submit={handleEdit}>
            <label for="name">Name:</label>
            <input bind:value={curr.name} type="text" class="input-form" name="name" required/>

            <div class="dialog-buttons">
                <button>Submit</button>
                <button on:click={() => curr = null}>Close</button>
            </div>
        </form>
    </DialogContent>
</DialogOverlay>

<div class="users-container">

</div>

<style lang="scss">

    .users-container{
        width: 100%;
        overflow: auto;
    }

</style>