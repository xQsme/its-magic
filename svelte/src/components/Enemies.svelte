<script lang="ts">
    import type { EnemyModel } from '../utils/models';
    import axios from 'axios';
    import { url } from '../utils/server';

    let enemies:EnemyModel[] = [];

    getEnemies();

    async function getEnemies() {
        let result:any = await axios.get(url + 'enemy');
        enemies = result.data;
        console.log(enemies);
    }
</script>

<div class="enemies-container">
    <div class="grid-container">
        {#each enemies as enemy}
            <div class="enemy">
                <img src={enemy.image} alt="enemy" class="enemy-image" />
                <p class="label">Name:</p>
                <p class="enemy-name">{enemy.name}</p>
                <p class="label">HP:</p>
                <p class="enemy-health">{enemy.hp}</p>
            </div>
        {/each}
    </div>
</div>

<style lang="scss">

    .enemies-container{
        width: 100%;
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
            background-color: #303030;
            display: flex;
            flex-direction: column;
            padding: 20px;
            cursor: pointer;

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
    }


</style>