# AlblifteData
Offene Datenbank (Open Data) der Skilifte auf der Schwäbischen Alb.

## Nutzung
Einbindung als [JSON](https://github.com/SkiLib/AlblifteData/data-export/json/Alblifte.json) Datei. Beispiel: Die Website [Alblifte.de](http://www.alblifte.de) verwendet Angaben aus diesem Repository.

## Beteiligung
Fehlermeldungen, Korrekturen und Erweiterungen werden gerne entgegengenommen: Als [GitHub Issue](https://github.com/SkiLib/AlblifteData/issues), als pull request oder als Nachricht an [Alblifte.de](http://www.alblifte.de/kontakt).

## Inhalt
Derzeit sind knapp 70 Lifte der Schwäbischen Alb enthalten.

**Identifikation**
| Attribut | Typ      | Beschreibung |
| ---      | ---      | --- |
| `ID`     | `String` | Identifier |
| `Name`   | `String` | Vollständiger Name des Lifts |

**Ortsangaben**
| Attribut     | Typ                  | Beschreibung |
| ---          | ---                  | --- |
| `Homepage`   |  `Url`               | Website |
| `GeoBreite`  |  `Float`             |  Geografische Breite |
| `GeoLaenge`  |  `Float`             |  Geografische Länge |
| `WebcamLink` |  `Url`               | Webpage: Webcam |
| `StatusLink` |  `Url`               | Webpage: Aktueller Betriebsstatus |
| `Telefon`    |  `Liste aus Strings` | Schnee- / Kontakt-Telefon |
| `Mietlift`   |  `Bool`              | Kann der Lift gemietet werden? |
| `EMail`      |  `E-Mail Adresse`    | Kontakt E-Mail Adresse |

**Infrastruktur**
| Attribut          | Typ     | Beschreibung |
| ---               | ---     | --- |
| `Kunstschnee`     |  `Bool` | Konstschnee vorhanden? |
| `Flutlicht`       |  `Bool` | Flutlicht vorhanden? |
| `Funpark`         |  `Bool` | Funpark vorhanden? |
| `Rodelhang`       |  `Bool` | Rodelhang vorhanden? |
| `Rodellift`       |  `Bool` | Rodellift vorhanden? |
| `Tubing`          |  `Bool` | Tubing vorhanden? |
| `Sommerbetrieb`   |  `Bool` | Sommerbetrieb möglich? |
| `Bikepark`        |  `Bool` | Bikepark vorhanden? |
| `Bullcart`        |  `Bool` | Bullcart vorhanden? |
| `Sommerrodelbahn` |  `Bool` | Sommerrodelbahn vorhanden? |

**Social Media**
| Attribut   | Typ    | Beschreibung |
| ---        | ---    | --- |
| `Facebook` |  `Url` | Facebook Page |
| `Twitter`  |  `Url` | Twitter Page |
| `YouTube`  |  `Url` | YouTube Page |

## Lizenz
[CC0-1.0](https://choosealicense.com/licenses/cc0-1.0)
