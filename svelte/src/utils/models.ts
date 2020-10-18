export interface AuthModel {
	email:string,
	username:string,
	role:string[],
    token:string,
}

export interface EnemyModel{
    id:number,
    name:string,
    hp:number,
    currentHP:number,
    mana:number,
    currentMana:number,
    damage:number,
    image:string,
}

export interface SpellModel{
    id:number,
    name:string,
    image:string,
}

export interface PlayerModel{
    name:string,
    hp:number,
    currentHP:number,
    mana:number,
    currentMana:number,
}