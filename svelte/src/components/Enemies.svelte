<script lang="ts">
    import type { EnemyModel } from '../utils/models';
    import axios from 'axios';
    import { url } from '../utils/server';
    import { DialogOverlay, DialogContent } from 'svelte-accessible-dialog';

    let enemies:EnemyModel[] = [];
    let curr:EnemyModel = null;
    let newEnemy:EnemyModel = {name: '', hp: 0, mana: 0, damage: 0, image: ''};
    let add=false;

    getEnemies();

    async function getEnemies() {
        let result:any = await axios.get(url + 'enemy');
        enemies = result.data;
    }
</script>

<DialogOverlay isOpen={add} onDismiss={() => add = false}>
    <DialogContent class="dialog" aria-label="Announcement">
        <form class="dialog-container">
            <label for="name">Name:</label>
            <input bind:value={newEnemy.name} type="text" class="input-form" name="name" required/>

            <label for="hp">HP:</label>
            <input bind:value={newEnemy.hp} type="number" class="input-form" name="hp" required/>

            <label for="mana">Mana:</label>
            <input bind:value={newEnemy.mana} type="number" class="input-form" name="mana" required/>

            <label for="damage">Damage:</label>
            <input bind:value={newEnemy.damage} type="number" class="input-form" name="damage" required/>

            <label for="image">Image:</label>
            <input bind:value={newEnemy.image} type="file" class="input-form" name="image" required/>

            <div class="dialog-buttons">
                <button>Submit</button>
                <button on:click={() => add = false}>Close</button>
            </div>
        </form>
    </DialogContent>
</DialogOverlay>

<div class="enemies-container">
    <div class="grid-container">
        <div class="add grid-item" on:click={() => add = true}>
            <i class="material-icons">add_circle</i>
        </div>
        {#each enemies as enemy}
            <div class="enemy grid-item" on:click={() => curr = enemy}>
                <img src={enemy.image} alt="enemy" class="enemy-image" />
                <p class="label">Name</p>
                <p class="enemy-name">{enemy.name}</p>
                <p class="label">HP</p>
                <p class="enemy-health">{enemy.hp}</p>
                <p class="label">Mana</p>
                <p class="enemy-name">{enemy.mana}</p>
                <p class="label">Damage</p>
                <p class="enemy-name">{enemy.damage}</p>
            </div>
        {/each}
    </div>
</div>

<style lang="scss">

    .dialog-container{
        display: flex;
        flex-direction: column;

        .dialog-buttons{
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
    }

    .enemies-container{
        width: 100%;
        overflow: auto;
    }

    .grid-container{
        max-width: 1200px;
        display: grid;
        grid-auto-rows: 1fr;
        grid-template-columns: repeat(4, 1fr); 
        grid-column-gap: 20px;
        grid-row-gap: 20px;
        width: 100%;
        padding: 20px;
        margin: auto;

        .enemy{

            p{
                margin: 0;
            }

            .label{
                opacity: 0.5;
                font-size: 14px;
                margin-top: 5px;
            }

            .enemy-image{
                max-width: 100%;
            }
        }

        .add{
            justify-content: center;
            align-items: center;

            i{
                font-size: 120px;
                transition: color .2s linear;
            }
        }

        .grid-item{
            display: flex;
            flex-direction: column;
            background-color: #303030;
            padding: 20px;
            cursor: pointer;
            transition: transform .2s, border-radius .2s;
        }

        .add:hover{
            i{
                color: orangered;
            }
        }

        .grid-item:hover{
            transform: scale(1.05);
            border-radius: 10px;
        }
    }
</style>