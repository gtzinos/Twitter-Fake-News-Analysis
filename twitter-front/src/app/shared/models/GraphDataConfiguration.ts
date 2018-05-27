export class GraphDataConfiguration {
  id: string;
  keys: [string];

  constructor(id: string, keys?: [string]) {
    this.id = id;
    this.keys = keys || [id];
  }
}
