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

<h1>Enemies</h1>